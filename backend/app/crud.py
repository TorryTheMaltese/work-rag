from sqlalchemy import select # type: ignore
from sqlalchemy.orm import Session # type: ignore

from app.models import Document, DocumentChunk
from app.schemas import DocumentCreate, DocumentChunkCreate
from app.services.embedding_service import create_embedding

def create_document(db: Session, document: DocumentCreate) -> Document:
    db_document = Document(filename=document.filename)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document


def get_document(db: Session) -> list[Document]:
    statement = select(Document)
    return db.scalars(statement).all()


def create_document_chunks(db: Session, document_id: int, chunks: list[str]) -> list[DocumentChunk]:
    db_chunks = []
    for index, chunk_text in enumerate(chunks):
        db_chunk = DocumentChunk(
            document_id=document_id,
            chunk_index=index,
            chunk_text=chunk_text,
            embedding=create_embedding(chunk_text)
        )
        db.add(db_chunk)
        db_chunks.append(db_chunk)
    db.commit()
    for db_chunk in db_chunks:
        db.refresh(db_chunk)
    return db_chunks


def search_similar_chunks(db: Session, query_embedding: list[float], limit: int = 3) -> list[DocumentChunk]:
    statement = (
        select(DocumentChunk)
        .where(DocumentChunk.embedding.is_not(None))
        .order_by(DocumentChunk.embedding.cosine_distance(query_embedding))
        .limit(limit)
        )
    return list(db.scalars(statement).all())