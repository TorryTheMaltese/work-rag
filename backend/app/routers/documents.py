from pathlib import Path
from shutil import copyfileobj

from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session # type: ignore

from app import crud, schemas
from app.database import get_db
from app.services.pdf_service import extract_text_from_pdf


BASE_DIR = Path(__file__).resolve().parents[3]
UPLOAD_DIR = BASE_DIR / "uploads"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

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

@router.post("/upload", response_model=schemas.DocumentRead, status_code=201)
def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="PDF 파일만 업로드 가능합니다.")

    if not file.filename:
        raise HTTPException(status_code=400, detail="파일 이름이 없습니다.")

    safe_filename = Path(file.filename).name
    file_path = UPLOAD_DIR / safe_filename

    try:
        with file_path.open("wb") as buffer:
            copyfileobj(file.file, buffer)

            document_data = schemas.DocumentCreate(filename=safe_filename)
            extracted_text=extract_text_from_pdf(file_path)
            print("추출된 글자 수: ", len(extracted_text))
            print("추출된 결과 일부: ", extracted_text[:500])

            return crud.create_document(db=db, document=document_data)
        
    except Exception:
        if file_path.exists():
            file_path.unlink()  # Remove the partially uploaded file

        db.rollback()  # Rollback the database session to avoid partial commits

        raise HTTPException(status_code=500, detail="파일 업로드에 실패했습니다.")

    finally:
        file.file.close()