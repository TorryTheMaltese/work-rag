from fastapi import FastAPI

app = FastAPI(
    title="Work RAG API",
    description="업무 문서 기반 RAG 챗봇 API",
    version="0.1.0",
)


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