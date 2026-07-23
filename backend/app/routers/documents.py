from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session # type: ignore

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

@router.post("",response_model=schemas.DocumentRead)
def create_document(document: schemas.DocumentCreate, db: Session = Depends(get_db)):
    return crud.create_document(db=db, document=document)

@router.get("", response_model=list[schemas.DocumentRead])
def read_documents(db: Session = Depends(get_db)):
    return crud.get_document(db=db)