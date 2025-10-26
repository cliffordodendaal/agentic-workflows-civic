This agentic workflow summarizes upliftment projects from civic PDFs using LangChain tools and agents.



Problem Local governments publish civic project data in PDFs. Residents and NGOs struggle to extract relevant insights.



Solution An agent that:



Loads civic PDFs



Retrieves relevant chunks using keyword match



Summarizes using GPT



Outputs a clean report



Stack LangChain v1.0+ Streamlit UI PDF chunking and retrieval Tool-decorated agent



Repo Structure agents/civic\_summary\_agent.py tools/file\_reader.py tools/retriever.py ui/streamlit\_app.py data/sample\_pdfs/



Run Locally streamlit run ui/streamlit\_app.py



Portfolio Signal Agentic orchestration Civic data use case

