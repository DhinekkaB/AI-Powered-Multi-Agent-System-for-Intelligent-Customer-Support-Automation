from utils.llm_helpers import get_llm

llm = get_llm()

def route_task(resolution):
    prompt = f"Based on this resolution, which team should handle this task: {resolution}"
    return llm(prompt)
