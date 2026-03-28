from phi.agent import Agent
from phi.model.groq import Groq
from os import getenv

from .web_agent import getWebSearchAgent
from .finance_agent import geFinanceAgent


def getMultiAgent():
    return Agent(
        team=[
            getWebSearchAgent(),
            geFinanceAgent()
        ],
        instructions=["Always display the data clearly"],
        model=Groq(
            api_key=getenv("GROQ_API_KEY"),
            id=getenv("MODEL_ID")
        ),
        show_tool_calls=True,
        markdown=True
    )