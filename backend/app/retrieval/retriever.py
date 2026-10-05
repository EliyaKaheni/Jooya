from langchain_core.documents import Document

from app.retrieval.search import search


def retrieve(query: str, limit: int | None = None) -> list[Document]:
    results = search(query, limit)

    documents = []

    for result in results:
        payload = result.payload or {}

        text = payload.get('text', '').strip()
        if not text:
            continue

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": payload.get("source", "unknown"),
                    "page": payload.get("page", "unknown"),
                    "page_chunk_index": payload.get(
                        "page_chunk_index",
                        "unknown",
                    ),
                    "chunk_id": payload.get(
                        "chunk_id",
                        "unknown",
                    ),
                    "score": result.score,
                },
            )
        )

    return documents