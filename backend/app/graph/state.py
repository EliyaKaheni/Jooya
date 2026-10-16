from langchain_core.documents import Document
from typing import TypedDict, Any

class RAGState(TypedDict):
    question: str
    contexts: list[Document]
    research_result: list[dict[str, Any]]
    answer: str