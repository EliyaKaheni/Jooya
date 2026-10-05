from fastapi import FastAPI

from app.retrieval.search import search
from app.schemas import Citation, QueryRequest, QueryResponse


app = FastAPI(
    title="JooYa Agentic RAG",
    version="0.1.0",
    description="Retrieval API for the Agentic Research Assistant.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/search", response_model=QueryResponse)
def search_documents(request: QueryRequest) -> QueryResponse:
    points = search(request.query, request.top_k)

    results = [
        Citation(
            score=float(point.score),
            source=str(point.payload.get("source", "")),
            page=int(point.payload.get("page", 0)),
            chunk_id=int(point.payload.get("chunk_id", 0)),
            text=str(point.payload.get("text", "")),
        )
        for point in points
    ]

    return QueryResponse(query=request.query, results=results)
