import os
import shutil
import argparse
from dotenv import load_dotenv
from datetime import datetime

from src.resume_parser import read_file_content, read_pdf_content
from src.api_handler import tailor_resume, extract_job_position
from src.utils import save_output, save_description_pdf, extract_section_text, build_ordered_section_content
from src.latex_compiler import compile_latex_to_pdf, move_auxiliary_files

load_dotenv()

def main(company, job_url):
    if os.getenv("DOCKER_USE"):
        output_path = os.getenv("DOCKER_OUTPUT_PATH")
    else:
        output_path = os.getenv("LOCAL_OUTPUT_PATH")

    resume_path = os.path.join(output_path, "latex-resume", "main.tex")

    applications_path = os.path.join(output_path, "applications", str(datetime.today().date()), company)
    job_description_path = os.path.join(applications_path, "job_description.pdf")

    # Save job description as PDF file
    save_description_pdf(job_url, job_description_path)

    # Read the LaTeX resume
    resume_text = read_file_content(resume_path)
    
    # Extract the job description text from the saved file
    job_description = read_pdf_content(job_description_path)

    # Extract position
    position = extract_job_position(job_description)
    if not position:
        raise Exception("No position returned")
    
    # Sanitize and format position name
    position = position.split()
    position = ["".join(char for char in word if char.isalnum()) for word in position]
    position = "_".join(word.lower() for word in position)

    # Add position as subfolder
    applications_path = os.path.join(applications_path, position)
    os.makedirs(applications_path, exist_ok=True)
    new_job_description_path = os.path.join(applications_path, "job_description.pdf")
    shutil.move(job_description_path, new_job_description_path)

    # Resume Sections
    sections_dict = {}
    section_names = set(["CONSTANT", "PROFESSIONAL_SUMMARY", "TECHNICAL_SKILLS", "EXPERIENCE", "EDUCATION", "CERTIFICATIONS", "PRACTICAL_PROJECTS"])

    # Extract sections from resume text.
    for section_name in section_names:
        extract_section_text(resume_text, section_name, sections_dict)
    
    # Tailor the resume sections to the job description using OpenAI API
    section_names.discard("CONSTANT") # Non changing content; Not to be tailored
    section_names.discard("EDUCATION") # Non changing content; Not to be tailored
    section_names.discard("PROFESSIONAL_SUMMARY") # To be tailored last based on experience and projects
    for section, content in sections_dict.items():
        if section in section_names:
            sections_dict[section] = tailor_resume(section, content, job_description)

    
    # Build experience content for tailoring summary
    tailored_experience = build_ordered_section_content(["PROFESSIONAL_SUMMARY", "TECHNICAL_SKILLS", "EXPERIENCE", "EDUCATION", "CERTIFICATIONS", "PRACTICAL_PROJECTS"], sections_dict)

    # Tailor the summary section last to the job description using OpenAI API
    sections_dict["PROFESSIONAL_SUMMARY"] = tailor_resume("PROFESSIONAL_SUMMARY", tailored_experience, job_description)
    

    # Build sections of tailored resume.
    tailored_resume = build_ordered_section_content(["CONSTANT", "PROFESSIONAL_SUMMARY", "TECHNICAL_SKILLS", "EXPERIENCE", "EDUCATION", "CERTIFICATIONS"], sections_dict)
    tailored_resume += "\n"
    tailored_resume += "%-------------------------------------------\n\\end{document}"
    
    tailored_resume_w_projects = build_ordered_section_content(["CONSTANT", "PROFESSIONAL_SUMMARY", "TECHNICAL_SKILLS", "EXPERIENCE", "EDUCATION", "CERTIFICATIONS", "PRACTICAL_PROJECTS"], sections_dict)
    tailored_resume_w_projects += "\n"
    tailored_resume_w_projects += "%-------------------------------------------\n\\end{document}"

    # Save the one page tailored resume in LaTeX format
    tailored_resume_tex_path = os.path.join(applications_path, f"{position}.tex")
    tailored_resume_w_projects_tex_path = os.path.join(applications_path, f"{position}_projects.tex")
    save_output(tailored_resume, tailored_resume_tex_path)
    save_output(tailored_resume_w_projects, tailored_resume_w_projects_tex_path)
    print(f"Tailored LaTeX resume saved at: {applications_path}")
    
    # Compile the LaTeX document to PDF
    compile_latex_to_pdf(tailored_resume_tex_path)
    compile_latex_to_pdf(tailored_resume_w_projects_tex_path)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Compile a LaTeX file and move auxiliary files.")
    parser.add_argument('company', type=str, help='Company name')
    parser.add_argument('job_url', type=str, help='URL of job description')
    # Parse the arguments
    args = parser.parse_args()

    # Call main function with parsed arguments
    main(os.getenv("company", args.company), os.getenv("job_url", args.job_url))