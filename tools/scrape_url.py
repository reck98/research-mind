import requests
from utils.config import TIMEOUT, HEADERS
from bs4 import BeautifulSoup
from langchain.tools import tool


@tool
def scrape_url_tool(url : str) -> dict:
    """
    Scrape a webpage and return its cleaned textual content.
    
    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        dict: A dictionary containing either:
            - url (str): The scraped webpage URL.
            - content (str): Extracted and cleaned text content,
              truncated to the first 3000 characters.

            Or, in case of failure:
            - error (str): Description of the error encountered
              during the request or parsing process.
    """
    
    try: 
        response = requests.get(
            url=url, 
            timeout=TIMEOUT,
            headers=HEADERS
        )
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        for tag in soup([
                "script",
                "style",
                "nav",
                "footer",
                "aside"
            ]):
            tag.decompose()
        
        content = soup.get_text(separator=" ", strip=True)[:3000]
        return {
            "url" : url,
            "content" : content
        }
    
    except Exception as e:
        return {
            "error" : str(e)
        }
        
        