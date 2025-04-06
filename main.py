from agents.input_agent import InputAgent
from agents.summary_agent import SummaryAgent
from agents.action_extraction_agent import ActionExtractionAgent
from agents.resolution_agent import ResolutionAgent
from agents.routing_agent import RoutingAgent
from agents.time_estimation_agent import TimeEstimationAgent
from agents.response_generator_agent import ResponseGeneratorAgent

if __name__ == "__main__":
    input_agent = InputAgent()
    summary_agent = SummaryAgent()
    action_agent = ActionExtractionAgent()
    resolution_agent = ResolutionAgent()
    routing_agent = RoutingAgent()
    time_agent = TimeEstimationAgent()
    response_agent = ResponseGeneratorAgent()

    # Flow
    user_input = input_agent.receive_input()
    summary = summary_agent.summarize(user_input)
    actions = action_agent.extract_actions(summary)
    resolution = resolution_agent.recommend_resolution(actions)
    routing = routing_agent.route_task(resolution)
    time = time_agent.estimate_resolution_time(routing)
    final_response = response_agent.generate_response(resolution, time)

    print("\n[Multi-Agent System Output]")
    print(f"User Query: {user_input}")
    print(f"Summary: {summary}")
    print(f"Actions: {actions}")
    print(f"Resolution: {resolution}")
    print(f"Routing: {routing}")
    print(f"Time Estimate: {time}")
    print(f"\nFinal Response:\n{final_response}")
