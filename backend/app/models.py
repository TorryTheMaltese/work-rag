from sqlalchemy import ForeignKey # type: ignore
from sqlalchemy.orm import Mapped, mapped_column # type: ignore
from pgvector.sqlalchemy import Vector # type: ignore

from app.database import Base

class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"<Document(id={self.id}, filename={self.filename!r})>"


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id: Mapped[int] = mapped_column(primary_key=True)
    document_id: Mapped[int] = mapped_column(ForeignKey("documents.id"))
    chunk_index: Mapped[int] = mapped_column()
    chunk_text: Mapped[str] = mapped_column()
    embedding: Mapped[list[float]] = mapped_column(Vector(1024), nullable=True)

    def __repr__(self) -> str:
        return f"<DocumentChunk(id={self.id}, document_id={self.document_id}, chunk_index={self.chunk_index})>"