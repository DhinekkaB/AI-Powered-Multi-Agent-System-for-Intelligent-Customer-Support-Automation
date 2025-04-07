from utils.llm_helpers import get_llm

llm = get_llm()

def extract_actions(summary):
    prompt = f"Extract key action items from this summary: {summary}"
    return llm(prompt)
