from app.llm.prompt import rag_answer

question = "What is Git?"
answer = rag_answer(question)

print(f'The question: {question}\n')
print(f'The answer: {answer}')