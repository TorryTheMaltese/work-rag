from fastapi import FastAPI
from sqlalchemy import select # type: ignore

from app.models import Document
from app.database import Base, SessionLocal,engine
from app.routers import documents, chat


app = FastAPI(
    title="Work RAG API",
    description="업무 문서 기반 RAG 챗봇 API",
    version="0.1.0"
)

app.include_router(documents.router)
app.include_router(chat.router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Work RAG API",
        "status": "running",
    }


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
    }