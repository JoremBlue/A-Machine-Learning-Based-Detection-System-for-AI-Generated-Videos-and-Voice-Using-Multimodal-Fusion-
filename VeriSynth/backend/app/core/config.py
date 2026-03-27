import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/deepfake_db")
    UPLOAD_DIR = os.getenv("UPLOAD_DIR", "/app/uploads")
    MODEL_WEIGHTS_DIR = os.getenv("MODEL_WEIGHTS_DIR", "/app/models")

settings = Settings()
