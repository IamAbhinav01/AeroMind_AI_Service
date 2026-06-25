import os
from dotenv import load_dotenv
from app.errors import ErrorHandler

load_dotenv()

PORT = os.getenv("PORT")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not PORT:
    raise ErrorHandler(
        "Missing configuration",
        status_code=500,
        detail="Environment variable PORT is required"
    )

if not GROQ_API_KEY:
    raise ErrorHandler(
        "Missing configuration",
        status_code=500,
        detail="Environment variable GROQ_API_KEY is required"
    )
