from app.errors import ErrorHandler
from app.prompts import parser_prompt
from app.config import get_groq_client

def extract_info(input_prompt:str) ->dict:
    try:
        result = parser_prompt.invoke({"requestQuery":input_prompt})
        model = get_groq_client()
        response = model.invoke(result)
        raw_output = response.content if has

    except ErrorHandler:
        raise
