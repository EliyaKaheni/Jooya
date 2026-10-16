import asyncio

from app.agents.research_agent import add_research
from app.graph.state import RAGState


async def main():
    state: RAGState = {
        "question": "What is Git?",
        "contexts": [],
        "research_result": [],
        "answer": "",
    }

    new_state = await add_research(state)

    print("\nQuestion:")
    print(new_state["question"])

    print("\nResearch Results:")
    for i, result in enumerate(new_state["research_result"], start=1):
        print(f"\n--- Result {i} ---")
        print("Title:", result["title"])
        print("URL:", result["url"])
        print("Content:", result["content"])
        print("Engine:", result["engine"])
        print("Score:", result["score"])


if __name__ == "__main__":
    asyncio.run(main())