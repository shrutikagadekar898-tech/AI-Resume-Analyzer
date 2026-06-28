import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_cover_letter_ai(name, job_role, company, resume_text):

    prompt = f"""
You are an expert HR recruiter and professional career coach.

Generate a professional ATS-friendly cover letter.

Candidate Name:
{name}

Job Role:
{job_role}

Company:
{company}

Resume:
{resume_text}

Instructions:
- Keep it professional.
- Keep it within 300 words.
- Highlight relevant skills.
- Mention enthusiasm for the role.
- End politely.
"""

    response = model.generate_content(prompt)

    return response.text