from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from dotenv import load_dotenv


class Settings(BaseSettings):
    # Qdrant
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "jooya_documents"

    # Embedding
    embedding_model: str = "BAAI/bge-m3"
    embedding_dimension: int = 1024

    # Chunking
    chunk_size: int = 500
    chunk_overlap: int = 50

    # Retrieval
    top_k: int = 5

    # LLM
    llm_model: str = "gpt-4o-mini"
    llm_temperature: float = 0.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

load_dotenv()
settings = get_settings()
