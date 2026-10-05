from uuid import NAMESPACE_URL, uuid5

from langchain_core.documents import Document
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from app.config import settings


client = QdrantClient(url=settings.qdrant_url)
COLLECTION_NAME = settings.qdrant_collection


def create_collection() -> None:
    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=settings.embedding_dimension,
                distance=Distance.COSINE,
            ),
        )


def _point_id(chunk: Document) -> str:
    source = chunk.metadata.get("source", "unknown")
    page = chunk.metadata.get("page", 0)
    chunk_id = chunk.metadata.get("chunk_id", 0)
    return str(uuid5(NAMESPACE_URL, f"{source}:{page}:{chunk_id}"))


def store_chunks(chunks: list[Document], embeddings) -> None:
    if len(chunks) != len(embeddings):
        raise ValueError("Number of chunks and embeddings must be equal")

    create_collection()

    points = [
        PointStruct(
            id=_point_id(chunk),
            vector=embedding.tolist(),
            payload={
                "text": chunk.page_content,
                **chunk.metadata,
            },
        )
        for chunk, embedding in zip(chunks, embeddings)
    ]

    if points:
        client.upsert(collection_name=COLLECTION_NAME, points=points)


def clear_collection() -> None:
    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)
    create_collection()
