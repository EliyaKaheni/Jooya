from qdrant_client.models import ScoredPoint

from app.config import settings
from app.ingestion.embedder import embed_texts
from app.vectorstore.qdrant import COLLECTION_NAME, client, create_collection


def search(query: str, limit: int | None = None) -> list[ScoredPoint]:
    if not query.strip():
        raise ValueError("query must not be empty")

    create_collection()
    query_embedding = embed_texts([query])[0]

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding.tolist(),
        limit=limit or settings.top_k,
        with_payload=True,
    )

    return response.points

