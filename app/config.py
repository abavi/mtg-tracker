from pydantic import BaseSettings
import os
from dotenv import load_dotenv

# Load enviroment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    app_name: str = "MTG Tracker"
    secret_key: str = os.getenv("SECRET KEY", "fallback-secret")
    database_url: str = os.getenv("DATABASE_URL","sqlite:///./mtg-tracker.db")

settings = Settings()