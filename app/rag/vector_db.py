from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

embeddings = HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorDB = Chroma(collection_name="quiz_rag", embedding_function=embeddings, persist_directory="./chroma_db")