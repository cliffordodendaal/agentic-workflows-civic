def get_relevant_chunks(query: str, chunks: list) -> str:
    relevant = [chunk.page_content for chunk in chunks if query.lower() in chunk.page_content.lower()]
    return "\n\n".join(relevant[:5])  # Return top 5 matches
