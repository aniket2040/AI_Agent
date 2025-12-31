import streamlit as st
from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool
import os
from dotenv import load_dotenv

# Load environment variables from .env file for local development
load_dotenv()

def get_api_keys():
    """Get API keys from Streamlit secrets or environment variables."""
    import os.path
    secrets_paths = [
        os.path.expanduser("~/.streamlit/secrets.toml"),
        ".streamlit/secrets.toml"
    ]
    secrets_exist = any(os.path.exists(path) for path in secrets_paths)
    
    if secrets_exist:
        try:
            TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
            GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
        except KeyError:
            st.error("API keys not found in Streamlit secrets.")
            st.stop()
    else:
        # Fallback to environment variables for local development
        TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
        GROQ_API_KEY = os.getenv('GROQ_API_KEY')
        if not TAVILY_API_KEY or not GROQ_API_KEY:
            st.error("Missing API keys. For local development, create a .env file with TAVILY_API_KEY and GROQ_API_KEY. For deployment, set them in Streamlit secrets.")
            st.stop()
    return TAVILY_API_KEY, GROQ_API_KEY

def tavily_search(query: str) -> str:
    TAVILY_API_KEY, GROQ_API_KEY = get_api_keys()
    
    # Set environment variable for Groq
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY
    
    agent = Agent(
        'groq:llama-3.1-8b-instant',
        tools=[tavily_search_tool(TAVILY_API_KEY)],
        system_prompt="Search tavily for the given query and return the result"
    )
    
    response = agent.run_sync(f"Search tavily for: {query}")
    return response
