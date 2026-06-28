from utils.skill_extractor import extract_skills


def calculate_professional_ats(resume_text):

    score = 0

    skills = extract_skills(resume_text)

    # ---------- Skills ----------
    score += min(len(skills) * 2, 40)

    # ---------- Projects ----------
    if "project" in resume_text.lower():
        score += 20

    # ---------- Education ----------
    if "education" in resume_text.lower():
        score += 10

    # ---------- Certifications ----------
    if "certification" in resume_text.lower() or "certifications" in resume_text.lower():
        score += 10

    # ---------- GitHub ----------
    if "github" in resume_text.lower():
        score += 5

    # ---------- LinkedIn ----------
    if "linkedin" in resume_text.lower():
        score += 5

    # ---------- Contact ----------
    if "@" in resume_text:
        score += 5

    if "+91" in resume_text or "phone" in resume_text.lower():
        score += 5

    return min(score, 100)


def get_ats_breakdown(resume_text):

    breakdown = {}

    skills = extract_skills(resume_text)

    breakdown["Skills"] = min(len(skills) * 2, 40)
    breakdown["Projects"] = 20 if "project" in resume_text.lower() else 0
    breakdown["Education"] = 10 if "education" in resume_text.lower() else 0
    breakdown["Certifications"] = 10 if (
        "certification" in resume_text.lower()
        or "certifications" in resume_text.lower()
    ) else 0
    breakdown["GitHub"] = 5 if "github" in resume_text.lower() else 0
    breakdown["LinkedIn"] = 5 if "linkedin" in resume_text.lower() else 0

    if "@" in resume_text and (
        "+91" in resume_text or "phone" in resume_text.lower()
    ):
        breakdown["Contact"] = 10
    else:
        breakdown["Contact"] = 0

    return breakdown