from app.llm.prompt import rag_answer
from app.graph.state import RAGState

def add_answer(state: RAGState) -> RAGState:
    question = state['question']
    contexts = state['contexts']
    research_results = state['research_result']

    answer = rag_answer(question, contexts, research_results)
    return {**state, 'answer':answer}
    