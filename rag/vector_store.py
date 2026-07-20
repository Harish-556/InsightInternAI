from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embeddings):
    return FAISS.from_texts(chunks, embeddings)