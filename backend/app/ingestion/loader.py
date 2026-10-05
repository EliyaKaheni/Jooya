from pathlib import Path

from langchain_core.documents import Document
from pypdf import PdfReader


def load_pdf(file_path: Path) -> list[Document]:
    if not file_path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    reader = PdfReader(str(file_path))
    documents: list[Document] = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        if not text:
            continue

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": file_path.name,
                    "page": page_number,
                },
            )
        )

    return documents
