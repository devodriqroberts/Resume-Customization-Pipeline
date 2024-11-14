import os
from src.pdf_generator import PdfGenerator

def save_output(content, output_path):
    """Save the tailored resume content to a specified output file.

    Args:
        content (str): Content string to be saved
        output_path (str): Path location to save content
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as file:
        file.write(content)

def save_description_pdf(url, job_description_path):
    """Save job description webpage as PDF file.

    Args:
        url (str): URL of webpage
        job_description_path (str): Path location to save pdf
    """
    os.makedirs(os.path.dirname(job_description_path), exist_ok=True)
    pdf_file = PdfGenerator([url]).main()
    # save pdf to file
    with open(job_description_path, "wb") as outfile:
        outfile.write(pdf_file[0])  # directly write bytes - Playwright

def extract_section_text(text, section_name, hashmap):
    """Extract section substring from a resume text

    Args:
        text (str): Resume text containing sections to extract
        section_name (str): Name of section
        hashmap (dict): Stores extracted section text
    """
    start_token = "%" + "-"*10 + section_name + "-"*10
    end_token = "%" + "-"*10 + "END_" + section_name + "-"*10

    start_index = text.index(start_token)
    end_token_length = len(end_token)
    end_index = text.index(end_token) + end_token_length + 1

    hashmap[section_name] = text[start_index:end_index]

def build_ordered_section_content(sections, content_dict):
    """Builds resume content in order of given list

    Args:
        sections (list): Ordered list of section names
        content_dict (dict): Dict of section names and content

    Returns:
        str: Concatenated string of section content
    """
    return "\n".join([content_dict[section] for section in sections])