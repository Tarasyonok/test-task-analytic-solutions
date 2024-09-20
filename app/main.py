from fastapi import FastAPI

from app.documents.router import router as router_documents

app = FastAPI(
    title="Работа с документами",
    root_path="/api",
)

app.include_router(router_documents)
