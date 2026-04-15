from phi.agent import Agent
from phi.model.groq import Groq
from os import getenv

from .insights_agent import getInsightsAgent
from .news_agent import getNewsImpactAgent


def getMultiAgent():
    return Agent(
        name="Finlactics-Multi-Agent",
        team=[
            getInsightsAgent(),
            getNewsImpactAgent()
        ],
        instructions=[
            "Combine outputs from all agents into a single structured response",
            "Always format output in the following sections:",
            "1. 📊 Investment Insights",
            "2. 📰 News Impact Analysis",
            "3. 🧠 Final Verdict (Bullish / Neutral / Bearish)",
            "Keep response concise, clear, and actionable"
        ],
        model=Groq(
            api_key=getenv("GROQ_API_KEY"),
            id=getenv("MODEL_ID")
        ),
        show_tool_calls=True,
        markdown=True
    )