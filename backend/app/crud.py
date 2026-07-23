from sqlalchemy import select # type: ignore
from sqlalchemy.orm import Session # type: ignore

from app.models import Document
from app.schemas import DocumentCreate

def create_document(db: Session, document: DocumentCreate) -> Document:
    db_document = Document(filename=document.filename)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document


def get_document(db: Session) -> list[Document]:
    statement = select(Document)
    return db.scalars(statement).all()