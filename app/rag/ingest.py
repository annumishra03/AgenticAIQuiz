from app.rag.vector_db import vectorDB


def add_documents(texts:List[str]):
    vectorDB.add_texts(texts)
    vectorDB.persist()