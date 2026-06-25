from fastapi import APIRouter, HTTPException
from app.services.parser import extract_info
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/ai")


class SearchQuery(BaseModel):
    query: str


@router.post("/semantic-search")
async def semantic_search(request: SearchQuery):
    try:
        return extract_info(request.query)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
