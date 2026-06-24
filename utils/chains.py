from utils.prompts import writer_prompt, critic_prompt
from langchain_groq import ChatGroq
from utils.config import GROQ_API_KEY
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(
    api_key=GROQ_API_KEY, 
    model="openai/gpt-oss-20b",
    temperature=0
)

writer_chain = writer_prompt | llm | StrOutputParser()
critic_chain = critic_prompt | llm | StrOutputParser()