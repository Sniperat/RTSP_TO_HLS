# 📹 FastAPI RTSP to HLS Streaming API

Ushbu ilova FastAPI asosida tuzilgan bo‘lib, RTSP oqimlarini HLS formatga o‘zgartirib, foydalanuvchiga `index.m3u8` URL ko‘rinishida taqdim etadi. API chaqiruvlari PostgreSQL bazasiga log qilinadi.

---

## 🚀 Ishga tushirish (Docker bilan)

### 1. Klonlash va o‘rnatish

```bash
git clone https://github.com/Sniperat/RTSP_TO_HLS.git
cd RTSP_TO_HLS
```

### 2. `.env` faylini yaratish

`.env` fayli quyidagicha bo‘lishi kerak:

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/streamdb
```

### 3. Docker Compose orqali ishga tushurish

```bash
docker-compose up --build
```

### 4. API hujjatlari uchun Swagger

Brauzerda oching:

```
http://localhost:8000/docs
```

---

## 📦 API foydalanish

### RTSP URL yuborish

```http
POST /stream
Content-Type: application/json

{
  "rtsp_url": "rtsp://your-camera-stream"
}
```

**Javob:**

```json
{
  "hls_url": "/streams/{id}/index.m3u8"
}
```

---

## 🧱 Texnologiyalar

* **FastAPI** — yuqori samarali web framework
* **PostgreSQL** — ma’lumotlar bazasi
* **SQLAlchemy** — ORM
* **Alembic** — migratsiya vositasi (opsional)
* **FFmpeg** — RTSP → HLS konversiya
* **Docker & Docker Compose** — konteynerlash

---

## ℹ️ Eslatma

* Foydalanilayotgan RTSP manba **jamoatchilikka ochiq** yoki sizda ruxsat bo‘lgan kamera bo‘lishi kerak.
* `ffmpeg` oqimni orqada fon rejimida kodlaydi (`subprocess.Popen`).

---

## 🤝 Muallif

Kamina 😊
