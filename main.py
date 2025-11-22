from config import get_openai_key

from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool


def main():
    client = OpenAIClient(api_key=get_openai_key())
    agent = Agent(client=client, name="HealthcareMAS Agent")

    response = agent.run("Ciao! Come posso aiutarti oggi nel settore sanitario?")

    print("Risposta dell'agente:")
    print(response)
        


if __name__ == "__main__":
    main()