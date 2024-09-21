import asyncio
import json
from datetime import datetime
from typing import Generator

import pytest
from httpx import AsyncClient
from sqlalchemy import insert

from app.config import settings
from app.database import Base, async_session_maker, engine
from app.main import app as fastapi_app
from app.documents.models import Document

from fastapi.testclient import TestClient
from httpx import AsyncClient
from app.main import app as fastapi_app

@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)

    documents = open_mock_json("documents")

    for document in documents:
        document["created_date"] = datetime.strptime(document["created_date"], "%Y-%m-%d %H:%M:%S")
    
    async with async_session_maker() as session:
        add_documents = insert(Document).values(documents)
        await session.execute(add_documents)
        await session.commit()


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac
        

@pytest.fixture(scope="function")
async def session():
    async with async_session_maker() as session:
        yield session
