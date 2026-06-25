import os
from dotenv import load_dotenv
from app.errors import ErrorHandler

load_dotenv()

PORT = os.getenv("PORT")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")
GROQ_TEMPERATURE = os.getenv("GROQ_TEMPERATURE")

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

if not GROQ_MODEL:
    raise ErrorHandler(
        "Missing configuration",
        status_code=500,
        detail="Environment variable GROQ_MODEL is required"
    )

if GROQ_TEMPERATURE is None:
    raise ErrorHandler(
        "Missing configuration",
        status_code=500,
        detail="Environment variable GROQ_TEMPERATURE is required"
    )
