from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List


def split_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List[str]:
    """
    Split raw text into overlapping chunks for embedding.

    Args:
        text:          Raw extracted text from the PDF.
        chunk_size:    Maximum characters per chunk.
        chunk_overlap: Characters shared between consecutive chunks.

    Returns:
        List of text chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""],
    )
    chunks = splitter.split_text(text)
    return chunks
