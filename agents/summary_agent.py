from utils.llm_helpers import get_llm

llm = get_llm()

def summarize_query(query):
    prompt = f"Summarize the following customer query: {query}"
    return llm(prompt)
