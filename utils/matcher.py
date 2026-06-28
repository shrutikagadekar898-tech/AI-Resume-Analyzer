from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.skill_extractor import extract_skills

def calculate_match(resume_text, jd_text):

    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(jd_text))

    if len(jd_skills) == 0:
        return 0

    matched = resume_skills.intersection(jd_skills)

    score = (len(matched) / len(jd_skills)) * 100

    return round(score, 2)


def compare_skills(resume_text, jd_text):

    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(jd_text))

    matched = sorted(list(resume_skills & jd_skills))
    missing = sorted(list(jd_skills - resume_skills))

    return matched, missing