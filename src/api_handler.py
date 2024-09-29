import os
from openai import OpenAI

def extract_job_position(job_description):
    """Call the OpenAI API to tailor the resume to the job description."""
    system_role_prompt = os.getenv("SYSTEM_ROLE_POSITION")

    prompt = (
        "Job Description(s):\n" + job_description + "\n\n"
    )

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_role_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    response_content = response.choices[0].message.content
    return response_content

def tailor_resume(section_name, resume_text, job_description):
    """Call the OpenAI API to tailor the resume to the job description."""
    print(f"Start tailoring {section_name} section")
    system_role_prompt_1 = os.getenv(f"SYSTEM_ROLE_{section_name}")
    system_role_prompt_2 = os.getenv("SYSTEM_LATEX_DOC_STRUCTURE")

    prompt = (
        "Resume (LaTeX):\n" + resume_text + "\n\n"
        "Job Description(s):\n" + job_description + "\n\n"
    )

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_role_prompt_1},
            {"role": "system", "content": system_role_prompt_2},
            {"role": "user", "content": prompt}
        ]
    )
    response_content = response.choices[0].message.content
    response_content = response_content.strip("```")
    response_content = response_content.strip("latex")
    return response_content