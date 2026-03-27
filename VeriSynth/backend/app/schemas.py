from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AnalysisBase(BaseModel):
    filename: str
    prediction: str
    confidence: float
    video_score: float
    audio_score: float
    scene_score: float

class AnalysisCreate(AnalysisBase):
    pass

class AnalysisResponse(AnalysisBase):
    id: int
    upload_time: datetime
    grad_cam_path: Optional[str] = None
    spectrogram_path: Optional[str] = None

    class Config:
        from_attributes = True
