from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY,GROQ_MODEL,GROQ_TEMPERATURE
from app.errors import ErrorHandler

__llm__instance:ChatGroq | None = None

def get_groq_client()->ChatGroq:
    global __llm__instance
    if __llm__instance is None:
        if not GROQ_API_KEY or not GROQ_MODEL:
            raise ErrorHandler(
                "Missing configuration",
        status_code=500,
        detail="GROQ_API_KEY and GROQ_MODEL must be set in the environment."
            )
    __llm__instance = ChatGroq(
        api_key=GROQ_API_KEY,model=GROQ_MODEL,
        temperature=GROQ_TEMPERATURE
    )
    return __llm__instance   