# AI-Powered Multi-Agent Customer Support System

A modular, intelligent customer support automation system powered by **LangChain**, **OpenAI**, **Pinecone**, and **FastAPI**. This system uses collaborative agents to streamline and automate support processes including summarization, action extraction, resolution recommendation, routing, and response generation.

---

## Problem Statement

Modern enterprises face increased customer support loads with slow response times, inefficient task routing, and inconsistent resolutions. This system solves that by enabling multiple AI agents to work together and automate each step in the support workflow.

---

## Features

- ✍️ Summarizes customer queries  
- ✅ Extracts actionable tasks  
- 🧠 Recommends resolutions using semantic search  
- 🔀 Routes tasks to appropriate teams  
- ⏱️ Estimates resolution time  
- 💬 Generates final customer response  

---

##  Multi-Agent Architecture

| Agent                 | Responsibility                                         |
|----------------------|---------------------------------------------------------|
| **SummarizerAgent**  | Uses OpenAI to summarize the customer query             |
| **ActionAgent**      | Extracts tasks/action items from the summary            |
| **ResolutionAgent**  | Uses Pinecone vector DB to recommend a past solution    |
| **RoutingAgent**     | Assigns task to the correct internal support team       |
| **TimeAgent**        | Predicts estimated resolution time                      |
| **ResponseAgent**    | Compiles the final response to be sent to the customer  |

---

## 🛠️ Technologies Used

- [LangChain](https://www.langchain.com/) – LLM Orchestration  
- [OpenAI API](https://openai.com) – Summarization, reasoning, generation  
- [Pinecone](https://www.pinecone.io/) – Semantic vector search  
- [FastAPI](https://fastapi.tiangolo.com/) – API development  
- [python-dotenv](https://pypi.org/project/python-dotenv/) – Env management  

---

## 📁 Project Structure

AI-Powered-Multi-Agent-System-for-Intelligent-Customer-Support-Automation/
├── main.py                  # FastAPI entrypoint
├── agents/
│   ├── summary_agent.py
│   ├── action_agent.py
│   ├── resolution_agent.py
│   ├── routing_agent.py
│   └── time_agent.py
├── memory/
│   └── vector_store.py      # Pinecone client
├── utils/
│   └── llm_helpers.py       # OpenAI wrappers
├── .env                     # For API keys
└── requirements.txt

