from app.graph.workflow import create_workflow

wf = create_workflow()

result = wf.invoke({'question': 'What is Git?'})
print(result)