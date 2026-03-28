from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from os import getenv


def getWebSearchAgent():
    return Agent(
        name="Web-Search-Agent",
        role="Search the web for information",
        model=Groq(
            api_key=getenv("GROQ_API_KEY"),
            id=getenv("MODEL_ID")
        ),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True
    )