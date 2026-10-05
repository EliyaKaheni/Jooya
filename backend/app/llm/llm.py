from langchain_openai import ChatOpenAI
from app.config import settings

def get_llm() -> ChatOpenAI:
    return ChatOpenAI(model=settings.llm_model, temperature=settings.llm_temperature)