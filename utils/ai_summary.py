from utils.skill_extractor import extract_skills

def generate_summary(resume_text, missing_skills):

    skills = extract_skills(resume_text)

    summary = f"""
Your resume contains {len(skills)} technical skills.

Strengths:
✅ Strong technical profile
✅ Projects included
✅ ATS friendly resume

"""

    if missing_skills:
        summary += "\nAreas to Improve:\n"

        for skill in missing_skills:
            summary += f"• Learn or add {skill}\n"

    else:
        summary += "\nExcellent! Your resume matches the job description."

    return summary