


import streamlit as st
from agent_utils import tavily_search

# -------------------------------
# Helper function to format output
# -------------------------------
def format_response(result):
    """
    Takes an AgentRunResult or string and returns clean markdown text.
    """
    # If result has .output attribute, extract it
    if hasattr(result, "output"):
        text = result.output
    else:
        text = str(result)

    # Optional: split into sentences for readability
    sentences = text.split(". ")
    formatted = "\n".join([f"- {s.strip()}" for s in sentences if s.strip()])
    return formatted

# -------------------------------
# Streamlit App Config
# -------------------------------
st.set_page_config(page_title="AI Search Agent", page_icon="🔍")

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🔍 AI Search Agent")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input for user query
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from agent
    with st.chat_message("assistant"):
        with st.spinner("Searching..."):
            result = tavily_search(prompt)   # returns AgentRunResult
            response = format_response(result)
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
