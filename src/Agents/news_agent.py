from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from os import getenv


def getNewsImpactAgent():
    return Agent(
        name="News-Impact-Agent",
        role="Analyze news and its impact on stocks",
        model=Groq(
            api_key=getenv("GROQ_API_KEY"),
            id=getenv("MODEL_ID")
        ),
        tools=[DuckDuckGo()],
        instructions=[
            "Search for recent news about the given company",
            "Summarize key headlines",
            "Analyze sentiment (Positive / Negative / Neutral)",
            "Explain how the news may impact stock price",
            "Focus on short-term and long-term impact",
            "Always include sources"
        ],
        show_tool_calls=True,
        markdown=True
    )