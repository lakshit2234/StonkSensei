import openai
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq


import os
import phi
from phi.playground import Playground, serve_playground_app

load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

web_search_agent=Agent(
    name="Web Search Agent",
    role="Searches the web for information",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,

)

finance_agent=Agent(
    name="Financial AI Agent",
    role="Provides financial information and analysis",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),

        ],
    instructions=["Use Tables to Display the Data"],
    show_tool_calls=True,
    markdown=True,
    )

app=Playground(agents=[finance_agent,web_search_agent]).get_app()


if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)
