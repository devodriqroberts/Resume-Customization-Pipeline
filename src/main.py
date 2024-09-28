import os
import argparse
from dotenv import load_dotenv

from src.resume_parser import read_file_content, read_rtf_content
from src.api_handler import tailor_resume
from src.utils import save_output, remove_first_line
from src.latex_compiler import compile_latex_to_pdf

load_dotenv()

def main(company, position):
    output_path = os.getenv("OUTPUT_PATH")
    resume_path = os.path.join(output_path, "latex-resume-main", "main.tex")
    job_description_path = os.path.join(output_path, company, f"{position}.rtf")
    tailored_resume_tex_path = os.path.join(output_path, company, f"{position}.tex")

    # Read the LaTeX resume
    resume_text = read_file_content(resume_path)
    
    # Extract the job description text from the saved file
    job_description = read_rtf_content(job_description_path)
    
    # Tailor the resume to the job description using OpenAI API
    tailored_resume = tailor_resume(resume_text, job_description)

    # Save the tailored resume in LaTeX format
    save_output(tailored_resume, tailored_resume_tex_path)
    remove_first_line(tailored_resume_tex_path)
    print(f"Tailored LaTeX resume saved at: {tailored_resume_tex_path}")
    
    # Compile the LaTeX document to PDF
    compile_latex_to_pdf(tailored_resume_tex_path)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Compile a LaTeX file and move auxiliary files.")
    parser.add_argument('company', type=str, help='Name of the company')
    parser.add_argument('position', type=str, help='Name of the position')

    # Parse the arguments
    args = parser.parse_args()

    # Call main function with parsed arguments
    main(args.company, args.position)