from striprtf.striprtf import rtf_to_text

def read_file_content(file_path):
    """Read the content of a file given its path."""
    with open(file_path, "r") as file:
        return file.read()
    
def read_rtf_content(file_path):
    """Read and extract text from an RTF file."""
    try:
        with open(file_path, "r") as file:
            rtf_content = file.read()
    except:
        raise Exception("Missing job description.")
    
    # Convert RTF content to plain text
    plain_text = rtf_to_text(rtf_content)
    
    return plain_text