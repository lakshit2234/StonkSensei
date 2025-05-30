from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

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

multi_ai_agent=Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)

