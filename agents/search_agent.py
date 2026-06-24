from langchain.agents import create_agent
from langchain_groq import ChatGroq
from utils.config import GROQ_API_KEY
from tools.web_search import web_search_tool


llm = ChatGroq(
    api_key=GROQ_API_KEY, 
    model="openai/gpt-oss-20b",
    temperature=0
)

def build_search_agent():
    return create_agent(
        llm, 
        tools=[web_search_tool], 
        system_prompt="Always include all the urls of the search results.",
    )





