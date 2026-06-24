from agents.search_agent import build_search_agent
from agents.reader_agent import build_reader_agent
from utils.chains import writer_chain, critic_chain
from langchain.messages import HumanMessage
from rich import print
from utils.config import EXTRA_LINES


def run_research_mind(topic : str) -> dict:
    """
    Execute the complete research workflow for a given topic.

    The function coordinates multiple agents and chains to:
    1. Search the web for relevant information.
    2. Select and scrape the most useful source.
    3. Generate a research report from the collected information.
    4. Critique and review the generated report.

    Args:
        topic (str): The research topic or question to investigate.

    Returns:
        dict: A dictionary containing:
            - search_result (str): Results returned by the search agent.
            - scraped_content (str): Detailed content extracted by the reader agent.
            - report (str): The generated research report.
            - critic (str): Feedback and evaluation of the report.
    """
    
    state = {}
    
    ## search agent 
    
    print(EXTRA_LINES)
    print("Search agent is thinking...")
    search_agent = build_search_agent()
    search_result = search_agent.invoke({"messages" : [
        HumanMessage(content=f"Find recent and reliable and detailed information about the topic: {topic}")
    ]})
    
    state["search_result"] = search_result["messages"][-1].content
    print(state["search_result"])
    print("Search agent is done")
    print(EXTRA_LINES)
    
    
    ## reader agent 
    print(EXTRA_LINES)
    print("Reader agent is thinking...")    
    
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({"messages" : [
        HumanMessage(
            content=
            f"Based on the following search results about '{topic}'\n"
            f"Pick the most relevant url and scrape it for deeper content \n \n"
            f"Search Results: \n"
            f"{state['search_result']}"
        )
    ]})
    
    state["scraped_content"] = reader_result["messages"][-1].content
    print(state["scraped_content"])
    print("Reader agent is done")
    print(EXTRA_LINES)
    
    ## writer chain 
    
    print(EXTRA_LINES)
    print("Writer chain is working...")
    
    research_combined = (
        f"Search Results: \n{state['search_result']}\n \n"
        f"Detailed Scraped Content : \n{state['scraped_content']}\n \n"
    )
    
    state['report'] = writer_chain.invoke({
        "topic" : topic, 
        "research" : research_combined
    })
    
    print(state['report'])
    print(EXTRA_LINES)
    
    print("Writer chain is done")
    
    ## critic chain 
    
    print(EXTRA_LINES)
    print("Critic chain is working...")
    
    state['critic'] = critic_chain.invoke({
        "report" : state['report']
    })
    
    print(state['critic'])
    
    print("Critic chain is done")
    print(EXTRA_LINES)
    
    return state
    

if __name__ == "__main__":
    
    topic = str(input("Enter the topic you want to investigate: "))
    
    run_research_mind(topic)
    
    
    
    
    
    

