from utils.llm_helpers import get_llm

llm = get_llm()

def estimate_resolution_time(summary):
    prompt = f"Estimate time required to resolve this issue: {summary}"
    return llm(prompt)
