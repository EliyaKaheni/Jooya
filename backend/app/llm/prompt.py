from langchain_core.documents import Document
from app.retrieval.retriever import retrieve
from app.llm.llm import get_llm

def build_rag_prompt(question: str, contexts: list[Document]) -> str:
    prompt = """You are a research assistant.

Your task is to answer the user's question using ONLY the information provided in the context section.

Rules:
1. Do not use information that is not present in the context.
2. Do not make assumptions or invent missing information.
3. If the context does not contain enough information to answer the question, clearly say that the provided context is not sufficient to answer the question.
4. For every factual claim, cite the corresponding source and page number using this format:
   [Source: <source> | Page: <page>]
5. Base your answer on the provided context, not on your prior knowledge.
"""

    prompt += "\n\nThis is the context section:\n"

    for ctx in contexts:
        source = ctx.metadata.get("source", "unknown")
        page = ctx.metadata.get("page", "unknown")

        prompt += f"\n[Source: {source} | Page: {page}]\n"
        prompt += f"{ctx.page_content}\n"

    prompt += f"""
    
The question is:
{question}

Answer the question based only on the provided context.
"""

    return prompt

def rag_answer(question: str, contexts: list[Document] | None = None ) -> str:
    if not contexts:
       contexts = retrieve(question)

    prompt = build_rag_prompt(question, contexts)

    llm = get_llm()

    response = llm.invoke(prompt)
    return str(response.content)
