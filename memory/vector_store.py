import os
import pinecone
from dotenv import load_dotenv
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv()
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENV"))

def get_vector_store():
    embeddings = OpenAIEmbeddings()
    return Pinecone(index=pinecone.Index(os.getenv("PINECONE_INDEX")), embedding=embeddings.embed_query)
