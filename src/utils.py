import os
from src.pdf_generator import PdfGenerator

def save_output(content, output_path):
    """Save the tailored resume content to a specified output file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as file:
        file.write(content)

def save_description_pdf(url, job_description_path):
    """Save job description webpage as PDF file."""
    os.makedirs(os.path.dirname(job_description_path), exist_ok=True)
    pdf_file = PdfGenerator([url]).main()
    # save pdf to file
    with open(job_description_path, "wb") as outfile:
        outfile.write(pdf_file[0].getbuffer())

def remove_first_line(file_path):
    """Remove the first line that contains only 'latex 'from a file."""
    # Read all lines of the file
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    if lines[0].strip() == "latex":
        # Remove the first line
        lines = lines[1:]
    
    # Write the remaining lines back to the file
    with open(file_path, "w") as file:
        file.writelines(lines)
    
    print(f"The first line has been removed from: {file_path}")