from sqlalchemy.orm import Mapped, mapped_column # type: ignore

from app.database import Base

class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column()
