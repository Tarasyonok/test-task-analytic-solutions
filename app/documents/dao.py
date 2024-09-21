from sqlalchemy import delete, text
from app.database import async_session_maker
from app.documents.models import Document


class DocumentDAO:
    @classmethod
    async def search(cls, search_text: str):
        async with async_session_maker() as session:
            # Говорим Postgres воспользоваться индексом
            await session.execute(text('SET enable_seqscan = OFF'))
            
            result = await session.execute(text("""
                SELECT *
                FROM documents
                WHERE text @@ plainto_tsquery(:search_text)
                ORDER BY created_date
                LIMIT 20;
            """), {"search_text": search_text})
            
            return result.mappings().all()
    
    @classmethod
    async def delete_by_id(cls, document_id: int):
        async with async_session_maker() as session:
            query = delete(Document).filter_by(id=document_id)
            await session.execute(query)
            await session.commit()
