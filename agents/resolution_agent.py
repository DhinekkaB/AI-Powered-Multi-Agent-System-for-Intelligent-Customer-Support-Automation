from memory.vector_store import get_vector_store

def recommend_resolution(summary):
    vectorstore = get_vector_store()
    docs = vectorstore.similarity_search(summary, k=1)
    return docs[0].page_content if docs else "No prior resolution found. Escalate to senior team."
