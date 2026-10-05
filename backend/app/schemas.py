from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    query: str = Field(min_length=1)
    top_k: int = Field(default=5, ge=1, le=20)


class Citation(BaseModel):
    score: float
    source: str
    page: int
    chunk_id: int
    text: str


class QueryResponse(BaseModel):
    query: str
    results: list[Citation]
