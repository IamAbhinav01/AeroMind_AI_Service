import json

from app.errors import ErrorHandler
from app.prompts import parser_prompt
from app.config import get_groq_client


def extract_info(input_prompt: str) -> dict:
    try:
        prompt_text = parser_prompt.format(requestQuery=input_prompt)
        model = get_groq_client()
        response = model.invoke(prompt_text)

        raw_output = getattr(response, "content", None)
        if raw_output is None:
            raise ErrorHandler(
                "Model response error",
                status_code=500,
                detail="The language model did not return any content."
            )

        if isinstance(raw_output, bytes):
            raw_output = raw_output.decode("utf-8")

        parsed = json.loads(raw_output.strip())
        return {"success": True, "data": parsed}

    except ErrorHandler:
        raise
    except json.JSONDecodeError as e:
        raise ErrorHandler(
            "Invalid AI output",
            status_code=500,
            detail=f"AI output was not valid JSON: {e}"
        )
    except Exception as e:
        raise ErrorHandler(
            "Extraction failed",
            status_code=500,
            detail=str(e)
        )
