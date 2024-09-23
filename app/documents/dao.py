import csv
from sqlalchemy import delete, text, insert
from app.database import async_session_maker
from app.documents.models import Document
from datetime import datetime


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
            
    @classmethod
    async def load_test_data(cls):
        async with async_session_maker() as session:
            with open('app/test_data.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar="'")
                print(next(reader))
                for row in reader:
                    query = insert(Document).values(
                        text=row[0],
                        created_date=datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S"),
                        rubrics=row[2][1:-1].replace('"', "").split(', '),
                    )
                    await session.execute(query)
                await session.commit()
