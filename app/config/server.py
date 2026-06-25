import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv("PORT")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")