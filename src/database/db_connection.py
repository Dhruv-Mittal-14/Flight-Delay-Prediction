from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env from project root
BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in .env file")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

def get_engine():
    return engine