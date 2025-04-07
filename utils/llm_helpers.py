import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()

def get_llm():
    return OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0)
