from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv
from Agents import finance_agent,web_agent,multi_agent
import os
load_dotenv()




def getPlayground()->Playground:
    app = Playground(
        agents=[
            finance_agent.geFinanceAgent(),
            web_agent.getWebSearchAgent(),
            multi_agent.getMultiAgent()
        ]
    ).get_app()
    return app
