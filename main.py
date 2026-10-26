import os
import shutil
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pipeline import run_preprocessing, extract_features, calculate_score

app = FastAPI(title="Voice Marker API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    filename = file.filename or "uploaded_audio"
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, filename)
    clean_path = None

    try:
        # Save uploaded file locally into the uploads/ directory
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Sequential ML pipeline execution: preprocessing -> extraction -> scoring
        clean_path = run_preprocessing(file_path)
        features = extract_features(clean_path)
        score = calculate_score(features, filename)

        return {
            "score": score,
            "status": "success",
            "features": features
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await file.close()
        # Clean up audio file after processing to save disk space
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except OSError:
                pass
        if clean_path and clean_path != file_path and os.path.exists(clean_path):
            try:
                os.remove(clean_path)
            except OSError:
                pass


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
