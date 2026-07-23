from pathlib import Path
from pypdf  import PdfReader # type: ignore

def extract_text_from_pdf(file_path: Path) -> str:
    reader = PdfReader(file_path)

    page_texts: list[str] = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            page_texts.append(text)
            
    return "\n\n".join(page_texts)