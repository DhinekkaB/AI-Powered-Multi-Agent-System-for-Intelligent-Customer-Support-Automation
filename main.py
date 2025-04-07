from fastapi import FastAPI
from pydantic import BaseModel
from agents.summary_agent import summarize_query
from agents.action_agent import extract_actions
from agents.resolution_agent import recommend_resolution
from agents.routing_agent import route_task
from agents.time_agent import estimate_resolution_time

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/process")
def process_query(req: QueryRequest):
    summary = summarize_query(req.query)
    actions = extract_actions(summary)
    resolution = recommend_resolution(summary)
    routing = route_task(resolution)
    time_estimate = estimate_resolution_time(summary)

    return {
        "summary": summary,
        "actions": actions,
        "resolution": resolution,
        "routing": routing,
        "estimated_time": time_estimate
    }
