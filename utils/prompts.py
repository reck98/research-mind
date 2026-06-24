from langchain_core.prompts import ChatPromptTemplate
from langchain.messages import HumanMessage, SystemMessage, AIMessage


writer_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(
        content="You are an expert research writer. Write clear, structured and insightful reports."
    ), 
    HumanMessage(
        content="""
        Write a detailed research report on the topic below.

        Topic: {topic}

        Research Gathered:
        {research}

        Structure the report as:
        - Introduction
        - Key Findings (minimum 3 well-explained points)
        - Conclusion
        - Sources (list all URLs found in the research)

        Be detailed, factual and professional.
        """
    )
])

critic_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(
        content="You are a sharp and constructive research critic. Be honest and specific."
    ), 
    HumanMessage(
        content=(
    """
        Review the research report below and evaluate it strictly.

        Report:
        {report}

        Respond in this exact format:

        Score: X/10

        Strengths:
        - ...
        - ...

        Areas to Improve:
        - ...
        - ...

        One line verdict:
        ...
    """
        )
    )
])

