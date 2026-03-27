from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
import os
import shutil
from . import models, schemas, crud
from .database import SessionLocal, engine
from .core.config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Deepfake Detection API")

# Ensure upload directory exists
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_video(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()):
    # Validate file extension
    allowed_extensions = [".mp4", ".avi", ".mov"]
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Invalid file type. Only MP4, AVI, MOV allowed.")

    # Save file temporarily
    file_path = os.path.join(settings.UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Create DB entry (placeholder)
    db = SessionLocal()
    analysis = schemas.AnalysisCreate(
        filename=file.filename,
        prediction="PENDING",
        confidence=0.0,
        video_score=0.0,
        audio_score=0.0,
        scene_score=0.0
    )
    db_analysis = crud.create_analysis(db, analysis)
    db.close()

    # TODO: Background task to process the video and update DB
    # We'll add ML processing in Phase 3

    return {"analysis_id": db_analysis.id, "message": "File uploaded. Processing will begin shortly."}

@app.get("/results/{analysis_id}")
def get_results(analysis_id: int):
    db = SessionLocal()
    analysis = crud.get_analysis(db, analysis_id)
    db.close()
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return analysis
