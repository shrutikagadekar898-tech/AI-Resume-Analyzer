TOTAL_SKILLS = 18

def calculate_ats_score(skills):
    score = (len(skills) / TOTAL_SKILLS) * 100
    return round(score, 2)