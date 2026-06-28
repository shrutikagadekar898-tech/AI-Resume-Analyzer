import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def rewrite_resume_ai(resume_text):

    prompt = f"""
You are an expert ATS Resume Writer.

Rewrite the following resume professionally.

Requirements:
- Improve grammar.
- Improve ATS score.
- Keep all factual information unchanged.
- Use strong action verbs.
- Make it concise and professional.

Resume:

{resume_text}
"""

    response = model.generate_content(prompt)

    return response.text