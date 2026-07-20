import fitz  # PyMuPDF


def load_pdf(file_path: str) -> str:
    """
    Extract all text from a PDF file.

    Args:
        file_path: Absolute path to the PDF file.

    Returns:
        A single string containing all extracted text.
    """
    doc  = fitz.open(file_path)
    text = ""
    for page_num, page in enumerate(doc, start=1):
        page_text = page.get_text()
        text += f"\n\n--- Page {page_num} ---\n\n{page_text}"
    doc.close()
    return text
