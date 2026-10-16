# Jooya

Jooya is an agentic Retrieval-Augmented Generation (RAG) system that answers questions using local PDF documents and web search results.

## Features

- PDF ingestion and token-based text chunking
- `BAAI/bge-m3` embeddings
- Qdrant vector database and semantic retrieval
- Web search via SearXNG
- LangGraph-based workflow
- Context-aware answer generation using local documents and web results
- Source citations for local documents and web results

## Architecture

```text
                 ┌──────────────┐
                 │ User Question│
                 └──────┬───────┘
                        │
              ┌─────────▼─────────┐
              │    LangGraph      │
              └─────────┬─────────┘
                        │
              ┌─────────▼─────────┐
              │  Retrieval Agent  │
              │      Qdrant       │
              └─────────┬─────────┘
                        │
              ┌─────────▼─────────┐
              │   Research Agent  │
              │     SearXNG       │
              └─────────┬─────────┘
                        │
              ┌─────────▼─────────┐
              │   Answer Agent    │
              │  LLM + Citations  │
              └─────────┬─────────┘
                        │
                 ┌──────▼───────┐
                 │ Final Answer │
                 └──────────────┘
```

## Tech Stack

- Python
- LangChain
- LangGraph
- Qdrant
- SearXNG
- Hugging Face Transformers
- `BAAI/bge-m3`
- GPT-6 Luna

## Configuration

Configure the required environment variables in a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

Qdrant and SearXNG are expected to be available at:

- Qdrant: `http://localhost:6333`
- SearXNG: `http://localhost:8080`

## Installation

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Testing

Run the RAG test:

```bash
cd backend
python -m tests.test_rag
```

Run the research agent test:

```bash
python -m tests.test_research
```
