# Jooya

Jooya is a **Retrieval-Augmented Generation (RAG)** system for answering questions from research papers and PDF documents.

## Features

* PDF document ingestion
* Token-based text chunking
* `BAAI/bge-m3` embeddings
* Qdrant vector database
* Semantic retrieval
* Context-aware RAG prompting
* Source and page citations
* GPT-6 Luna for answer generation
* Modular architecture for future multi-agent support

## Architecture

```text
PDF
 │
 ▼
Loader
 │
 ▼
Splitter
 │
 ▼
Embedding (BGE-M3)
 │
 ▼
Qdrant
 │
 ▼
Retriever
 │
 ▼
RAG Prompt
 │
 ▼
GPT-6 Luna
 │
 ▼
Answer + Citations
```

## Project Structure

```text
Jooya/
├── .env
├── backend/
│   ├── app/
│   │   ├── config.py
│   │   ├── ingestion/
│   │   ├── vectorstore/
│   │   ├── retrieval/
│   │   └── llm/
│   └── tests/
└── README.md
```

## Tech Stack

* **Python**
* **LangChain**
* **Qdrant**
* **PyPDF**
* **Hugging Face Transformers**
* **BAAI/bge-m3**
* **GPT-6 Luna**

## Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Qdrant is expected to be available at:

```text
http://localhost:6333
```

## Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the RAG test:

```bash
cd backend
python -m tests.test_rag
```

## Current Status

* [x] PDF ingestion
* [x] Chunking
* [x] Embeddings
* [x] Qdrant storage
* [x] Semantic retrieval
* [x] RAG prompt
* [x] LLM integration
* [x] Source/page citations

### Planned

* [ ] Reranking
* [ ] Query rewriting
* [ ] Multi-agent architecture
* [ ] Answer evaluation
* [ ] Research and verification agents
* [ ] API and frontend
