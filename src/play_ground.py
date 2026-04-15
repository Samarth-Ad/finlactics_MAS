from phi.playground import Playground
from dotenv import load_dotenv

from Agents.insights_agent import getInsightsAgent
from Agents.news_agent import getNewsImpactAgent
from Agents.multi_agent import getMultiAgent

load_dotenv()


def getPlayground() -> Playground:
    playground = Playground(
        agents=[
            getInsightsAgent(),
            getNewsImpactAgent(),
            getMultiAgent()
        ]
    )
    return playground.get_app()