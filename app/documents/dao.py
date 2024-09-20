from sqlalchemy import text
from app.database import async_session_maker


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
