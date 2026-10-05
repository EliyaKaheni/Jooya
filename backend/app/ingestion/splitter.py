from langchain_core.documents import Document
from transformers import AutoTokenizer

from app.config import settings


tokenizer = AutoTokenizer.from_pretrained(settings.embedding_model)


def split_document(
    documents: list[Document],
    chunk_size: int | None = None,
    chunk_overlap: int | None = None,
) -> list[Document]:
    chunk_size = chunk_size or settings.chunk_size
    chunk_overlap = chunk_overlap or settings.chunk_overlap

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be >= 0 and smaller than chunk_size")

    chunks: list[Document] = []

    for page_index, page in enumerate(documents):
        tokens = tokenizer.encode(
            page.page_content,
            add_special_tokens=False,
        )

        start = 0
        chunk_index = 0

        while start < len(tokens):
            end = min(start + chunk_size, len(tokens))
            chunk_tokens = tokens[start:end]
            text = tokenizer.decode(chunk_tokens, skip_special_tokens=True).strip()

            if text:
                chunks.append(
                    Document(
                        page_content=text,
                        metadata={
                            **page.metadata,
                            "page_chunk_index": chunk_index,
                        },
                    )
                )

            chunk_index += 1
            if end == len(tokens):
                break
            start = end - chunk_overlap

    # Global chunk index makes citations/debugging easier.
    for index, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = index

    return chunks
