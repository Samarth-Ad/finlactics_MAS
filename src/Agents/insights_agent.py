from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from os import getenv

def getInsightsAgent():
    return Agent(
        name="Insights-Agent",
        role="Provide deep investment insights and recommendations",
        model=Groq(
            api_key=getenv("GROQ_API_KEY"),
            id=getenv("MODEL_ID")
        ),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True
            )
        ],
        instructions=[
            "Analyze the stock using available tools",
            "Summarize analyst recommendations clearly",
            "Explain fundamentals in simple terms",
            "Highlight risks and opportunities",
            "Give a final verdict: Bullish / Neutral / Bearish",
            "Keep output concise but insightful"
        ],
        show_tool_calls=True,
        markdown=True
    )