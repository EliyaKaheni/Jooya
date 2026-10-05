from app.retrieval.retriever import retrieve


questions = [
    "What is Git?",
    "What is the purpose of git commit?",
    "How does git push work?",
]

for question in questions:
    print(f"\n{'=' * 80}")
    print(f"QUESTION: {question}")
    print(f"{'=' * 80}")

    contexts = retrieve(question, limit=5)

    for i, doc in enumerate(contexts, start=1):
        print(f"\n--- Context {i} ---")
        print(f"Source: {doc.metadata['source']}")
        print(f"Page: {doc.metadata['page']}")
        print(f"Chunk: {doc.metadata['page_chunk_index']}")
        print(f"Score: {doc.metadata['score']:.4f}")
        print(doc.page_content[:300])