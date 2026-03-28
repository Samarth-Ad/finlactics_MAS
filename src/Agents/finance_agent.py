from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from os import getenv


def geFinanceAgent():
    return Agent(
        name="Finance-Agent",
        role="Handles stock data, analyst recommendations, and financial metrics",
        model=Groq(
            api_key=getenv("GROQ_API_KEY"),
            id=getenv("MODEL_ID")
        ),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True,
                company_news=True
            )
        ],
        instructions=["Use tables to display the data"],
        show_tool_calls=True,  # ✅ fixed typo
        markdown=True
    )