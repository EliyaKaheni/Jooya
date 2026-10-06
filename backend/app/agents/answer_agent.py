from app.llm.prompt import rag_answer
from app.graph.state import RAGState

def add_answer(state: RAGState) -> RAGState:
    question = state['question']
    contexts = state['contexts']

    answer = rag_answer(question, contexts)
    return {**state, 'answer':answer}
    