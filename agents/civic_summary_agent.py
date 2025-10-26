from openai import OpenAI
from tools.file_reader import load_pdf_chunks
from tools.retriever import get_relevant_chunks

# Load and chunk civic upliftment PDFs
chunks = load_pdf_chunks("data/sample_pdfs")

def summarize_upliftment(query: str) -> str:
    """Summarize civic upliftment projects based on a natural-language query."""
    relevant = get_relevant_chunks(chunks, query)
    joined = "\n\n".join(relevant)
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a civic upliftment analyst."},
            {"role": "user", "content": f"Summarize the following data based on the query: '{query}'\n\n{joined}"}
        ]
    )
    return response.choices[0].message.content

# Expose for Streamlit
executor = lambda inputs: {"output": summarize_upliftment(inputs["input"])}
