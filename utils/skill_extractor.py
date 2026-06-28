import pandas as pd

skills_df = pd.read_csv("skills.csv")

SKILLS = skills_df["Skill"].dropna().str.lower().tolist()


def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill.title())

    return sorted(list(set(found)))