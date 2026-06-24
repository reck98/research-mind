from langchain.tools import tool
from tavily import TavilyClient
from utils.config import TAVILY_API_KEY


tavily = TavilyClient(api_key=TAVILY_API_KEY)


@tool
def web_search_tool(query: str) -> list[dict]:
    """
    Search the web using Tavily and return the top results.

    Args:
        query (str): The search query to look up on the web.

    Returns:
        list[dict]: A list of search results where each result contains:
            - title (str): Title of the webpage.
            - url (str): URL of the webpage.
            - content (str): Short snippet of the webpage content.
    """

    try:
        response = tavily.search(
            query=query,
            max_results=5
        )

        output = []

        for r in response["results"]:
            output.append({
                "title": r["title"],
                "url": r["url"],
                "content": r["content"][:300]
            })

        return output

    except Exception as e:
        return [{
            "error": str(e)
        }]
        
        
    
    
    
    
    