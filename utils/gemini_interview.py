import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_interview_questions(job_role):

    prompt = f"""
You are a Senior Technical Interviewer.

Generate 10 interview questions for the following role:

{job_role}

Include:
- Technical Questions
- HR Questions
- Coding Questions
- Scenario Based Questions

Format as a numbered list.
"""

    response = model.generate_content(prompt)

    return response.text