import os
import json
import argparse
from dotenv import load_dotenv

from src.resume_parser import read_file_content, read_pdf_content
from src.api_handler import tailor_resume
from src.utils import save_output, remove_first_line, save_description_pdf
from src.latex_compiler import compile_latex_to_pdf

load_dotenv()

def main(company, job_url):
    output_path = os.getenv("OUTPUT_PATH")
    resume_path = os.path.join(output_path, "latex-resume", "main.tex")

    applications_path = os.path.join(output_path, "applications", company)
    job_description_path = os.path.join(applications_path, "job_description.pdf")

    # Save job description as PDF file
    save_description_pdf(job_url, job_description_path)

    # Read the LaTeX resume
    resume_text = read_file_content(resume_path)
    
    # Extract the job description text from the saved file
    job_description = read_pdf_content(job_description_path)
    
    # Tailor the resume to the job description using OpenAI API
    json_response = tailor_resume(resume_text, job_description)

    if not json_response.strip():
        raise ValueError("Received an empty response from tailor_resume")

    try:
        json_response = json_response.strip("json")
        json_response = json_response.strip()

        # Escape backslashes
        escaped_json_response = json_response.replace("\\", "\\\\")
        escaped_json_response = escaped_json_response.replace("\n", "\\n")
        response = json.loads(json_response)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON response: {e}")

    # Extract necessary fields
    tailored_resume = response["resume"]
    position = response["position"]

    # Sanitize and format position name
    position = position.split()
    position = ["".join(char for char in word if char.isalnum()) for word in position]
    position = "_".join(word.lower() for word in position)

    # Rename PDF File
    os.rename(job_description_path, job_description_path.replace("job_description", f"{position}_description"))

    # Save the tailored resume in LaTeX format
    tailored_resume_tex_path = os.path.join(applications_path, f"{position}.tex")
    save_output(tailored_resume, tailored_resume_tex_path)
    remove_first_line(tailored_resume_tex_path)
    print(f"Tailored LaTeX resume saved at: {tailored_resume_tex_path}")
    
    # Compile the LaTeX document to PDF
    compile_latex_to_pdf(tailored_resume_tex_path)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Compile a LaTeX file and move auxiliary files.")
    parser.add_argument('company', type=str, help='Company name')
    parser.add_argument('job_url', type=str, help='URL of job description')

    # Parse the arguments
    args = parser.parse_args()

    # Call main function with parsed arguments
    main(args.company, args.job_url)