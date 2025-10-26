import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agents.civic_summary_agent import executor

st.set_page_config(page_title="Civic Summary Agent", layout="wide")
st.title("Civic Summary Agent")
st.markdown("Summarize civic upliftment projects using natural language queries.")

query = st.text_input("Enter your query:", placeholder="e.g. What projects are planned for Ward 4?")
if query:
    with st.spinner("Thinking..."):
        response = executor({"input": query})
        st.markdown("### Summary")
        st.write(response["output"])
