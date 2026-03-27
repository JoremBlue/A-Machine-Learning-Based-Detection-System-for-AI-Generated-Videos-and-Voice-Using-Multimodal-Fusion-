from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from .database import Base

class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    upload_time = Column(DateTime(timezone=True), server_default=func.now())
    prediction = Column(String)  # "REAL" or "FAKE"
    confidence = Column(Float)
    video_score = Column(Float)
    audio_score = Column(Float)
    scene_score = Column(Float)
    grad_cam_path = Column(Text, nullable=True)  # path to saved image
    spectrogram_path = Column(Text, nullable=True)
