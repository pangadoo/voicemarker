# Voice Marker 🎙️

**Voice Marker** (VocalPulse) is an AI-powered vocal health tracking application designed to detect early signs of vocal strain and fatigue before irreversible damage occurs. Built for voice-dependent professionals—such as teachers, singers, call-center operators, and public speakers—it offers a simple 10-second daily vocal check on any smartphone or computer microphone.

---

## 🌟 Key Features

- **In-Browser Audio Capture:** Records 10 seconds of raw voice audio using the Web Audio API without automatic gain control or echo cancellation distortions.
- **Client-Side WAV Encoding:** Directly encodes raw PCM audio buffers into standard 16-bit WAV format entirely in vanilla JavaScript—no heavy audio SDKs required.
- **Vocal Health Scoring:** Calculates a 0–100 health score with interactive visual feedback (Healthy, Mild Strain, Strained).
- **Acoustic Feature Extraction:** Analyzes key voice biomarkers including jitter, shimmer, and vocal energy.
- **7-Day Trend Tracking & Actionable Recovery:** Visualizes weekly voice health history and provides actionable vocal hygiene tips (hydration, humming exercises, vocal rest).
- **Resilient Fallback Mode:** Seamlessly switches to simulated feedback if microphone access is unavailable or if the backend is unreachable.

---

## 🏗️ Architecture & Tech Stack

```text
┌─────────────────────────────────┐
│     Frontend (Web App)          │
│  HTML5 + Vanilla JS + CSS3      │
│  Web Audio API & WebGL Shaders  │
└────────────────┬────────────────┘
                 │ POST /analyze (multipart/form-data: WAV)
                 ▼
┌─────────────────────────────────┐
│     Backend (FastAPI)           │
│  Uvicorn ASGI Server            │
│  CORS-enabled REST API          │
└────────────────┬────────────────┘
                 │ Sequential Pipeline
                 ▼
┌─────────────────────────────────┐
│     Audio & ML Pipeline         │
│  Audio Preprocessing            │
│  Feature Extraction (Jitter...) │
│  Vocal Health Scoring Engine    │
└─────────────────────────────────┘
```

- **Frontend:** Pure HTML5, CSS3, and Vanilla JavaScript (`index.html`) with a WebGL animated cloud shader background and zero external JavaScript frameworks.
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) with [Uvicorn](https://www.uvicorn.org/).
- **Containerization:** Docker (`python:3.10-slim` with `libsndfile1` & `ffmpeg` system packages).
- **Deployment:** Ready for [Render](https://render.com/) or [Railway](https://railway.app/).

---

## 📁 Project Structure

```text
.
├── index.html          # Single-page web frontend (audio recording, WebGL, trend dashboard)
├── main.py             # FastAPI backend with CORS and /analyze endpoint
├── pipeline.py         # ML pipeline stubs (preprocessing, acoustic extraction, scoring)
├── requirements.txt    # Python backend dependencies
├── Dockerfile          # Multi-stage container configuration with audio dependencies
├── .dockerignore       # Excludes virtual environments, temporary audio, and cache
└── .gitignore          # Git exclusion rules
```

---

## 🚀 Getting Started

### 1. Running the Frontend

The frontend is a lightweight, zero-dependency single-page application:

- **Quick Start:** Double-click or open `index.html` in any modern web browser (Chrome, Firefox, Safari, Edge).
- **Local Web Server (Recommended for microphone permissions):**
  ```bash
  # Using Python's built-in HTTP server:
  python -m http.server 3000
  ```
  Then navigate to `http://localhost:3000`.

> **Note:** In `index.html`, the backend endpoint URL is configured via `API_URL`:
> ```javascript
> var API_URL = 'https://voicemarker-y93d.onrender.com'; // or 'http://localhost:8000' for local backend
> ```

---

### 2. Running the Backend Locally

#### Prerequisites
- Python 3.10+ installed

#### Setup & Launch

1. **Create and activate a virtual environment:**
   ```bash
   # Windows (PowerShell):
   python -m venv .venv
   .\.venv\Scripts\activate

   # macOS / Linux:
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the development server:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **API Documentation:**
   - Interactive Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Alternative ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

### 3. Running with Docker

Build and run the containerized backend with system audio dependencies (`libsndfile1` and `ffmpeg`):

```bash
# Build the Docker image
docker build -t voicemarker-backend .

# Run the container (binds to port 8000, supports dynamic $PORT)
docker run -p 8000:8000 -e PORT=8000 voicemarker-backend
```

---

## 📡 API Reference

### `POST /analyze`

Analyzes an uploaded voice recording and computes vocal health metrics.

- **Content-Type:** `multipart/form-data`
- **Request Body:**
  | Field  | Type         | Description                                |
  |--------|--------------|--------------------------------------------|
  | `file` | `UploadFile` | Audio file recording (e.g., WAV, MP3, M4A) |

- **Sample Request (cURL):**
  ```bash
  curl -X POST "http://localhost:8000/analyze" \
       -F "file=@voice_sample.wav"
  ```

- **Sample JSON Response:**
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

- **Response Attributes:**
  - `score` *(integer)*: Vocal health score from 0 to 100.
  - `status` *(string)*: Execution status (`success`).
  - `features` *(object)*: Acoustic parameters extracted from the audio waveform.

---

## 🔒 Privacy & Safety

- Audio files uploaded for analysis are processed in a temporary container directory and deleted immediately upon analysis completion.
- Voice Marker is a wellness screening aid and is not intended as a substitute for professional clinical or medical diagnosis.
