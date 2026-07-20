import os
import tempfile
from streamlit.runtime.uploaded_file_manager import UploadedFile


def save_uploaded_file(uploaded_file: UploadedFile) -> str:
    """
    Save a Streamlit-uploaded file to a temporary location on disk.

    Streamlit's UploadedFile is an in-memory buffer; PyMuPDF needs a real
    file path, so we persist it temporarily.

    Args:
        uploaded_file: File object from st.file_uploader.

    Returns:
        Absolute path to the saved temporary file.
    """
    suffix = os.path.splitext(uploaded_file.name)[-1]  # e.g. ".pdf"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getbuffer())
        return tmp.name


def cleanup_temp_file(file_path: str) -> None:
    """
    Remove a temporary file from disk.

    Args:
        file_path: Path returned by save_uploaded_file.
    """
    if file_path and os.path.exists(file_path):
        os.remove(file_path)
