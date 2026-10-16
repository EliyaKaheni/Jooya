from app.research.search import SearXNGSearch
from app.graph.state import RAGState

BASE_URL = 'http://localhost:8080'

async def add_research(state: RAGState) -> RAGState:
    question = state["question"]

    search_client = SearXNGSearch(BASE_URL)

    results = await search_client.search(question)

    return {**state, "research_result": results}