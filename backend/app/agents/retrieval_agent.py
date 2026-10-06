from app.graph.state import RAGState
from app.retrieval.retriever import retrieve

def add_contexts(state: RAGState) -> RAGState:
    question = state['question']

    contexts = retrieve(question)
    
    return {**state, 'contexts':contexts}