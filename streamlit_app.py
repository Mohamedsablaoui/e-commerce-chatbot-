"""
streamlit_app.py — the browser chat UI for our agent.

Run it with:   streamlit run streamlit_app.py
(NOT `python streamlit_app.py` — streamlit needs its own launcher.)
"""

import streamlit as st

from app.agent import ask_agent

st.set_page_config(page_title="TechStore Assistant", page_icon="🛍️")
st.title("🛍️ TechStore Assistant")
st.caption("Ask me about our products (prices, stock, brands) or our policies (shipping, returns, warranty).")

# st.session_state keeps the conversation across reruns (Streamlit reruns the whole
# script on every message — session_state is how we remember past messages).
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show the conversation so far.
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# The input box at the bottom. Returns the text when the user hits Enter.
if prompt := st.chat_input("Ask about products or policies..."):
    # 1. show + store the user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. get the agent's answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = ask_agent(prompt)
        st.markdown(answer)

    # 3. store the assistant's message
    st.session_state.messages.append({"role": "assistant", "content": answer})