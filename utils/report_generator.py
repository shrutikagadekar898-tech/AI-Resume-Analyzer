import os
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    ats_score,
    match_score,
    skills,
    matched_skills,
    missing_skills,
    suggestions,
):

    # Project root path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    reports_dir = os.path.join(base_dir, "reports")

    os.makedirs(reports_dir, exist_ok=True)

    filename = os.path.join(reports_dir, "ATS_Report.pdf")

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("AI Resume Analyzer Report", styles["Title"]))
    story.append(Paragraph(f"ATS Score : {ats_score}%", styles["Normal"]))
    story.append(Paragraph(f"Match Score : {match_score}%", styles["Normal"]))

    story.append(Paragraph("<br/><b>Skills Found</b>", styles["Heading2"]))
    for skill in skills:
        story.append(Paragraph(skill, styles["Normal"]))

    story.append(Paragraph("<br/><b>Matching Skills</b>", styles["Heading2"]))
    for skill in matched_skills:
        story.append(Paragraph(skill, styles["Normal"]))

    story.append(Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"]))
    for skill in missing_skills:
        story.append(Paragraph(skill, styles["Normal"]))

    story.append(Paragraph("<br/><b>Suggestions</b>", styles["Heading2"]))
    for suggestion in suggestions:
        story.append(Paragraph(suggestion, styles["Normal"]))

    doc.build(story)

    return filename