import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")

if not GROQ_API_KEY:
    print("WARNING: GROQ_API_KEY is not set.")
if not DATABASE_URL:
    print("WARNING: DATABASE_URL is not set.")
