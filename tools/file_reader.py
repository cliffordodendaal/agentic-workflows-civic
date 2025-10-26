import os
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError

def load_pdf_chunks(folder_path: str) -> list:
    """Load and chunk all PDFs in the given folder into simple text blocks."""
    chunks = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            path = os.path.join(folder_path, filename)
            try:
                reader = PdfReader(path)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        chunks.append(text.strip())
            except PdfReadError:
                print(f"⚠️ Skipping unreadable PDF: {filename}")
    return chunks
