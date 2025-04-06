## 🧠 Multi-Agent Customer Support System

This project implements a modular, AI-powered multi-agent system designed to streamline customer support operations in large enterprises. Each agent is responsible for a specific task in the support pipeline, allowing seamless task automation and faster resolution times.

---

## 🔍 Problem Statement
Modern enterprises face challenges with:
- Slow and inconsistent responses
- Manual ticket routing and prioritization
- Inability to utilize historical resolutions efficiently

Our solution introduces a multi-agent architecture to:
- Automatically summarize queries
- Extract action items
- Recommend resolutions
- Route tasks intelligently
- Estimate and reduce resolution time

---

## 🚀 System Overview
The architecture consists of the following intelligent agents:

1. **InputAgent** – Simulates customer query intake.
2. **SummaryAgent** – Summarizes the key points from the query.
3. **ActionExtractionAgent** – Extracts tasks to be performed.
4. **ResolutionAgent** – Recommends a resolution strategy.
5. **RoutingAgent** – Determines the appropriate team for task routing.
6. **TimeEstimationAgent** – Estimates time required to solve the issue.
7. **ResponseGeneratorAgent** – Forms the final response to the customer.

---

## 🛠 Technologies Used
- Python 3
- Modular OOP-based Agent Design

---

## 🧩 Folder Structure
```
multi_agent_customer_support/
├── agents/
│   ├── input_agent.py
│   ├── summary_agent.py
│   ├── action_extraction_agent.py
│   ├── resolution_agent.py
│   ├── routing_agent.py
│   ├── time_estimation_agent.py
│   └── response_generator_agent.py
└── main.py
```

---

## 🧪 Demo Output
```
[Multi-Agent System Output]
User Query: I have been charged twice for my last order. Please help!
Summary: Summary: Customer reports double charge on recent order.
Actions: ['Check transaction history', 'Initiate refund']
Resolution: Verify duplicate charge and issue refund if confirmed.
Routing: Task routed to: Billing Team
Time Estimate: Estimated resolution time: 2 hours

Final Response:
Dear Customer,

Verify duplicate charge and issue refund if confirmed.
Estimated resolution time: 2 hours

Thank you for your patience.
```

---

## ▶️ Running the Project
```bash
cd multi_agent_customer_support
python main.py
```

---

## 📦 Future Improvements
- Integrate with actual ticketing systems (e.g., Jira, Zendesk)
- Use LLMs for summarization & intent recognition
- Add web UI for customer input

---

## 🤖 Authors
Developed for a customer support automation hackathon challenge.

---

## 📄 License
MIT License

---
