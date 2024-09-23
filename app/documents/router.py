
from fastapi import APIRouter

from app.documents.dao import DocumentDAO


router = APIRouter(
    prefix="/documents",
    tags=["Документы"],
)


@router.get("")
async def search(search_text: str):
    return await DocumentDAO.search(search_text=search_text)


@router.delete("/{document_id}")
async def delete_document(document_id: int):
    await DocumentDAO.delete_by_id(document_id=document_id)
    return f"Элемент с id {document_id} удалён"

@router.post("/load_data")
async def load_data():
    await DocumentDAO.load_test_data()
    return "Тестовые данные загружены"
