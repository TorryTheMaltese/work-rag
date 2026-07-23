from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session # type: ignore

from app import crud, schemas
from app.database import get_db
from app.services.embedding_service import create_embedding
from app.services.llm_service import generate_answer

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)


@router.post("", response_model=schemas.ChatResponse)
def chat(
    request: schemas.ChatRequest,
    db: Session = Depends(get_db),
):
    query_embedding = create_embedding(request.question)

    chunks = crud.search_similar_chunks(
        db=db,
        query_embedding=query_embedding,
        limit=request.limit,
    )

    contexts = [chunk.chunk_text for chunk in chunks]
    answer = generate_answer(question=request.question, contexts=contexts)

    return schemas.ChatResponse(
        answer=answer,
        question=request.question,
        sources=[
            schemas.ChatSource(
                document_id=chunk.document_id,
                chunk_index=chunk.chunk_index,
                chunk_text=chunk.chunk_text,
            )
            for chunk in chunks
        ],
    )