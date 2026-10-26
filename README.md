# Voice Marker 🎙️

Voice Marker is an AI-powered vocal health tracking application backend built with **FastAPI**. It processes audio recordings to extract acoustic features (such as jitter and shimmer) and evaluates vocal strain and fatigue scores.

## Tech Stack
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Containerization:** Docker (`python:3.10-slim` with `libsndfile1` & `ffmpeg`)
- **Deployment:** Render / Railway / Cloud containers

---

## Getting Started

### Local Development

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   # Windows:
   .\.venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

4. Interactive API documentation is available at:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

---

## Docker Deployment

Build and run the Docker container:

```bash
docker build -t voicemarker-backend .
docker run -p 8000:8000 -e PORT=8000 voicemarker-backend
```

---

## API Endpoints

### `POST /analyze`
Upload an audio file for vocal health analysis.

- **Request:** `multipart/form-data` with `file: UploadFile`
- **Response:**
  ```json
  {
    "score": 94,
    "status": "success",
    "features": {
      "jitter": 1.2,
      "shimmer": 3.4
    }
  }
  ```
