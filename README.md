# 🤖 StockSensei: Your Agentic AI for Financial Intelligence

**StockSensei** is an Agentic AI system that combines real-time financial data analysis with web search capabilities to provide deep insights on stocks, market trends, and financial news. Built using [phidata](https://docs.phidata.io/), LLMs from Groq, and tools like YFinance and DuckDuckGo.

---

## 🚀 Features

- 🔍 **Live Web Search**: Uses DuckDuckGo to fetch fresh financial news and updates.
- 📊 **Stock Insights**: Real-time stock prices, fundamentals, and analyst recommendations via Yahoo Finance.
- 🧠 **Agentic Architecture**: Two AI agents (Finance & Web Search) work as a team.
- 📈 **Streaming LLM Responses**: Powered by Groq's `deepseek-r1-distill-llama-70b`.
- 🧪 **Playground UI**: Interact visually with agents in a FastAPI-based frontend.

---

## 🧱 Tech Stack

- **[phidata](https://docs.phidata.io/)** – Agent orchestration framework
- **Groq LLMs** – Fast & cost-effective transformer models
- **FastAPI + Uvicorn** – For the web-based playground
- **DuckDuckGo API** – For real-time web results
- **Yahoo Finance (yfinance)** – Stock, fundamentals, analyst ratings

---

## 📂 Project Structure

```bash
.
├── financial_agent.py     # Script to run agents from terminal
├── playground.py          # Runs FastAPI Playground UI
├── .env                   # Contains API keys
├── requirements.txt       # Python dependencies
└── README.md              # You are here
