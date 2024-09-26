import os
from openai import OpenAI

def tailor_resume(resume_text, job_description):
    """Call the OpenAI API to tailor the resume to the job description."""
    role = os.getenv("SYSTEM_ROLE")

    prompt = (
        "Resume (LaTeX):\n" + resume_text + "\n\n"
        "Job Description(s):\n" + job_description + "\n\n"
    )

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt}
        ]
    )
    response_content = response.choices[0].message.content.strip("```")
    return response_content