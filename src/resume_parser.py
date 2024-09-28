import fitz

def read_file_content(file_path):
    """Read the content of a file given its path."""
    try:
        with open(file_path, "r") as file:
            return file.read()
    except:
        raise Exception("Issue reading resume latex file.")

def read_pdf_content(file_path):
    """Read and extract text from a PDF file."""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text
