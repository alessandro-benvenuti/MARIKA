from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool
from config import get_openai_key

client = OpenAIClient(api_key=get_openai_key())

def get_client() -> OpenAIClient:
    """Restituisce il client OpenAI configurato"""
    return client