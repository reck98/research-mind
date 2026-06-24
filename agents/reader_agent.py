from langchain.agents import create_agent
from langchain_groq import ChatGroq
from utils.config import GROQ_API_KEY
from tools.scrape_url import scrape_url_tool


llm = ChatGroq(
    api_key=GROQ_API_KEY, 
    temperature=0
)

def build_reader_agent():
    return create_agent(
        llm, 
        tools=[scrape_url_tool]
    )