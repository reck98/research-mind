from utils.prompts import writer_prompt, critic_prompt
from langchain_groq import ChatGroq
from utils.config import GROQ_API_KEY
from langchain_core.output_parsers import StrOutputParser
from groq import RateLimitError

llm = ChatGroq(
    api_key=GROQ_API_KEY, 
    model="openai/gpt-oss-20b",
    temperature=0
).with_retry(
    retry_if_exception_type=(RateLimitError,),
    wait_exponential_jitter=True,
    stop_after_attempt=5,
)

writer_chain = writer_prompt | llm | StrOutputParser()
critic_chain = critic_prompt | llm | StrOutputParser()