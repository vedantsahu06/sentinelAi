from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.agents import create_agent
from agent_system.state.sentinel_state import SentinelState
import os

load_dotenv()


structured_llm = ChatGroq(
    model="llama-3.1-8b-instant",
    
    temperature=0.0,
    max_retries=5,
    max_tokens=2000,

)


 




