import os
import secrets
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Vercel must define SECRET_KEY for persistent sessions; the fallback only
    # keeps public routes from crashing while configuration is being completed.
    SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_hex(32)
    MONGO_URI = os.getenv("MONGO_URI")
    JWT_SECRET = os.getenv("JWT_SECRET")