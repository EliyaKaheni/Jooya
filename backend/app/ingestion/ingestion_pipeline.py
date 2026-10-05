from pathlib import Path

from app.ingestion.embedder import embed_texts
from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_document
from app.vectorstore.qdrant import store_chunks


def ingest_pdf(file_path: Path) -> int:
    documents = load_pdf(file_path)
    chunks = split_document(documents)
    embeddings = embed_texts([chunk.page_content for chunk in chunks])
    store_chunks(chunks, embeddings)
    return len(chunks)
