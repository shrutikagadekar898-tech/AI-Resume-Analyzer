from utils.skill_extractor import extract_skills

def generate_summary(resume_text, ats, match_score, missing_skills):

    skills = extract_skills(resume_text)

    summary = f"""
📄 Resume Analysis Summary

⭐ ATS Score : {ats}%

🎯 Resume Match : {match_score}%

🛠 Skills Found : {len(skills)}

----------------------------------

Strengths
✅ ATS Friendly Resume
✅ Projects Included
✅ Technical Skills Present

"""

    if missing_skills:
        summary += "\nAreas to Improve:\n"

        for skill in missing_skills:
            summary += f"• Add {skill}\n"
    else:
        summary += "\n🎉 Excellent! No important skills are missing."

    return summary
    