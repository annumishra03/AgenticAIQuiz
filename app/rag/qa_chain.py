from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from app.rag.retriever import get_context

llm = ChatOllama(model='llama3', temperature=0)

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI tutor
Use the context below to answer the question.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
""")

def rag_answer(question: str):
    context = get_context(question)
    chain = prompt | llm
    response = chain.invoke({
        "context":context,
        "question": question
    })
    return response.content