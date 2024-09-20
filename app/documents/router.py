
from fastapi import APIRouter

from app.documents.dao import DocumentDAO


router = APIRouter(
    prefix="/documents",
    tags=["Документы"],
)


@router.get("")
async def full_text_search(search_text: str):
    return await DocumentDAO.search(search_text=search_text)