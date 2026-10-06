from langgraph.graph.state import CompiledStateGraph
from app.agents.retrieval_agent import add_contexts
from langgraph.graph import START, END, StateGraph
from app.agents.answer_agent import add_answer
from app.graph.state import RAGState

def create_workflow() -> CompiledStateGraph:
    graph_builder = StateGraph(RAGState)

    graph_builder.add_node('retrieve', add_contexts)
    graph_builder.add_node('answer', add_answer)

    graph_builder.add_edge(START, 'retrieve')
    graph_builder.add_edge('retrieve', 'answer')
    graph_builder.add_edge('answer', END)

    graph = graph_builder.compile()
    return graph