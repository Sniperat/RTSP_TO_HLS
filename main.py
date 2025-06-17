from fastapi import FastAPI, Request
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import subprocess
import uuid
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/streamdb")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class APICallLog(Base):
    __tablename__ = "api_call_logs"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    rtsp_url = Column(String)
    user_agent = Column(String)

Base.metadata.create_all(bind=engine)

class StreamRequest(BaseModel):
    rtsp_url: str

@app.post("/stream")
def stream_video(req: StreamRequest, request: Request):
    db = SessionLocal()
    log = APICallLog(rtsp_url=req.rtsp_url, user_agent=request.headers.get("user-agent"))
    db.add(log)
    db.commit()
    db.close()

    stream_id = str(uuid.uuid4())
    output_dir = f"streams/{stream_id}"
    os.makedirs(output_dir, exist_ok=True)
    
    command = [
        "ffmpeg",
        "-i", req.rtsp_url,
        "-c:v", "copy",
        "-f", "hls",
        f"{output_dir}/index.m3u8"
    ]
    subprocess.Popen(command)
    
    return {"hls_url": f"/streams/{stream_id}/index.m3u8"}
