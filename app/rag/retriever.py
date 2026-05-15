from app.rag.vector_db import vectorDB


def get_context(query:str):
    docs = vectorDB.similarity_search(query, k=3)

    return "\n".join([d.page_content for d in docs])