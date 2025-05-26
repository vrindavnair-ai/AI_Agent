#python3 -m venv venv  -- to create virtual environment in mac os
#source venv/bin/activate -- to activate the virtual environment

from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv #create an .env file to store APIs
from phi.tools.yfinance import YFinanceTools

agent = Agent(model=Groq(id="llama-3.3-70b-versatile"), #it has static data. that is data till a particular time
              tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)], #Agent uses tools to fetch latest information
              #tools is an array because it can use multiple tools
              show_tool_calls=True,
              markdown=True,
              instructions=["Use Tables to display data"],
              debug_mode=True, #optional to check step by step process
              )

#sometimes it won't work well as llama 3.3 is opensource model and it is not as good as openai.

agent.print_response("Summarize and compare analyst recommendation and fundamentals for TESLA and NVIDIA")