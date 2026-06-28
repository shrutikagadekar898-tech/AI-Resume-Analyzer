import streamlit as st
from utils.gemini_rewriter import rewrite_resume_ai
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from utils.gemini_interview import generate_interview_questions
from utils.gemini_cover_letter import generate_cover_letter_ai
from utils.ai_summary import generate_summary
from utils.pdf_reader import extract_text
from utils.skill_extractor import extract_skills
from utils.matcher import calculate_match, compare_skills
from utils.ats_score import calculate_professional_ats, get_ats_breakdown
from utils.report_generator import generate_report

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

st.sidebar.markdown("""
<div style="
background:linear-gradient(90deg,#2563eb,#7c3aed);
padding:18px;
border-radius:18px;
text-align:center;
font-size:30px;
font-weight:bold;
color:white;
box-shadow:0 6px 15px rgba(0,0,0,.3);
margin-bottom:20px;">
📄 AI Resume Analyzer
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.success("📄 Resume Upload")
st.sidebar.success("⭐ ATS Score")
st.sidebar.success("🎯 Job Match")
st.sidebar.success("📑 PDF Report")

# ---------------- Main ---------------- #
st.markdown("""
<h1>🤖 AI Resume Analyzer</h1>
<p style="text-align:center;color:#374151;font-size:20px;">
AI Powered Resume Screening • ATS Score • Match Job Description • Improve Resume
</p>
""", unsafe_allow_html=True)

st.info("""
🚀 Upload your Resume and compare it with any Job Description.

✔ ATS Score

✔ Resume Match

✔ Missing Skills

✔ AI Suggestions

✔ PDF Report
""")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    skills = extract_skills(resume_text)

    ats = calculate_professional_ats(resume_text)

    st.subheader("📄 Resume Text")

    st.text_area(
        "",
        resume_text,
        height=250
    )

    st.subheader("🛠 Skills Found")

    programming = ["Java", "Python", "C", "C++"]
    backend = ["Spring Boot", "Hibernate", "JPA", "Servlet", "JSP"]
    database = ["MySQL", "PostgreSQL", "MongoDB"]
    frontend = ["HTML", "CSS", "JavaScript", "React"]

    categories = {
      "💻 Programming": programming,
      "⚙ Backend": backend,
      "🗄 Database": database,
      "🌐 Frontend": frontend,
}

    for title, techs in categories.items():

       selected = [skill for skill in skills if skill in techs]

       if selected:

          st.markdown(f"### {title}")

          html = ""

          for skill in selected:
             html += f'<span class="skill-chip">{skill}</span>'

          st.markdown(html, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("⭐ Professional ATS Score")

    fig = go.Figure(
        go.Indicator(
        mode="gauge+number",
        value=ats,
        number={"suffix": "%"},
        title={"text": "<b>ATS Score</b>", "font": {"size": 26}},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#2563EB"},
            "steps": [
                {"range": [0, 40], "color": "#FECACA"},
                {"range": [40, 70], "color": "#FDE68A"},
                {"range": [70, 100], "color": "#BBF7D0"}
            ],
            "threshold": {
                "line": {"color": "red", "width": 4},
                "thickness": 0.75,
                "value": ats
            }
        }
    )
    )

    fig.update_layout(
    height=350,
    margin=dict(l=20, r=20, t=50, b=20)
   )

    st.plotly_chart(fig, use_container_width=True)

# Score Message
    if ats >= 85:
      st.success("🏆 Excellent ATS Score! Your resume is highly ATS-friendly.")
    elif ats >= 70:
        st.warning("⭐ Good ATS Score. A few improvements can make it stronger.")
    else:
        st.error("⚠️ Low ATS Score. Add more relevant keywords and projects.")
    # ATS Chart

    st.markdown("---")

    st.subheader("📊 ATS Score Chart")

    fig, ax = plt.subplots(figsize=(5,3))

    ax.bar(["ATS Score"], [ats])

    ax.set_ylim(0,100)

    st.pyplot(fig)

    # ---------------- Job Description ---------------- #

    st.markdown("---")

    st.subheader("📋 Job Description")

    job_description = st.text_area(
        "Paste Job Description Here",
        height=180
    )

    match_score = 0
    matched = []
    missing = []

    if job_description:

        match_score = calculate_match(
            resume_text,
            job_description
        )

        matched, missing = compare_skills(
            resume_text,
            job_description
        )

        st.subheader("🎯 Resume Match")

        st.progress(int(match_score))

        st.success(f"{match_score}% Match")

        # ---------------- Dashboard Summary ---------------- #

    st.markdown("---")
    st.subheader("📊 Dashboard Summary")

    total_skills = len(skills)
    matched_skills = len(matched)
    missing_skills = len(missing)

    st.markdown(f"""
<div class="summary-container">

<div class="summary-card">
<h2>⭐ ATS Score</h2>
<h1>{ats}%</h1>
</div>

<div class="summary-card">
<h2>🎯 Job Match</h2>
<h1>{match_score}%</h1>
</div>

<div class="summary-card">
<h2>🛠 Skills</h2>
<h1>{len(skills)}</h1>
</div>

<div class="summary-card">
<h2>❌ Missing</h2>
<h1>{len(missing)}</h1>
</div>

</div>
""", unsafe_allow_html=True)

        # ---------------- ATS Score Breakdown ---------------- #

    st.markdown("---")
    st.subheader("📊 ATS Score Breakdown")

    breakdown = get_ats_breakdown(resume_text)

    for section, score in breakdown.items():
         st.write(f"**{section} : {score} Marks**")
         st.progress(score / 40 if section == "Skills" else score / 20 if section == "Projects" else score / 10)
            # ---------------- Metrics ---------------- #

    # ---------------- Resume Strengths ---------------- #

    st.markdown("---")

    st.subheader("✅ Resume Strengths")

    strengths = []

    if "github" in resume_text.lower():
        strengths.append("GitHub Profile Found")

    if "linkedin" in resume_text.lower():
        strengths.append("LinkedIn Profile Found")

    if "project" in resume_text.lower():
        strengths.append("Projects Section Available")

    if "certification" in resume_text.lower() or "certifications" in resume_text.lower():
        strengths.append("Certifications Included")

    if "java" in resume_text.lower():
        strengths.append("Java Skills Present")

    if "spring boot" in resume_text.lower():
        strengths.append("Spring Boot Skills Present")

    if strengths:
        for item in strengths:
            st.success(item)
    else:
        st.info("No strengths detected.")

    st.markdown("---")
    st.subheader("📋 Resume Section Analysis")

    sections = {
        "Education": "education",
        "Projects": "project",
        "Skills": "skill",
        "Certifications": "certification",
        "GitHub": "github",
        "LinkedIn": "linkedin",
        "Experience": "experience"
    }

    for section, keyword in sections.items():
        if keyword in resume_text.lower():
            st.success(f"✅ {section} Found")
        else:
            st.error(f"❌ {section} Missing")
    # ---------------- Resume Suggestions ---------------- #

    st.markdown("---")

    st.subheader("💡 Resume Improvement Suggestions")

    suggestions = []

    if "docker" not in resume_text.lower():
        suggestions.append("Learn and add Docker")

    if "aws" not in resume_text.lower():
        suggestions.append("Learn AWS")

    if "microservices" not in resume_text.lower():
        suggestions.append("Learn Microservices")

    if "internship" not in resume_text.lower():
        suggestions.append("Add Internship Experience")

    if suggestions:
        for item in suggestions:
            st.markdown(
    f"""
<div style="
background:#fff7ed;
padding:15px;
margin:10px 0;
border-radius:12px;
border-left:6px solid #f97316;
font-size:17px;
font-weight:600;
color:#9a3412;">
💡 {item}
</div>
""",
unsafe_allow_html=True)
    else:
        st.success("Excellent Resume!")

# ---------------- AI Resume Summary ---------------- #

    st.markdown("---")
    st.subheader("🤖 AI Resume Summary")
    summary = generate_summary(
    resume_text,
    ats,
    match_score,
    missing
)
    st.info(summary)
    # ---------------- Skills Comparison ---------------- #

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matching Skills")

        if matched:
            for skill in matched:
                st.markdown(
    f"""
    <div style="
        background:#dcfce7;
        padding:10px;
        border-radius:10px;
        margin:5px;
        color:#166534;">
        ✅ {skill}
    </div>
    """,
    unsafe_allow_html=True
)
        else:
            st.info("No matching skills found.")

    with col2:

        st.subheader("❌ Missing Skills")

        if missing:
            for skill in missing:
                st.markdown(
    f"""
    <div style="
        background:#fee2e2;
        padding:10px;
        border-radius:10px;
        margin:5px;
        color:#991b1b;">
        ❌ {skill}
    </div>
    """,
    unsafe_allow_html=True
)
        else:
            st.success("No missing skills 🎉")


                # ---------------- Skills Pie Chart ---------------- #

    st.markdown("---")
    st.subheader("🥧 Skills Distribution")

    if matched or missing:

        fig, ax = plt.subplots(figsize=(5, 5))

        sizes = [len(matched), len(missing)]
        labels = ["Matching Skills", "Missing Skills"]

        ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )

        ax.axis("equal")

        st.pyplot(fig)

    # ---------------- Course Recommendations ---------------- #

    st.markdown("---")
    st.subheader("🎓 Recommended Courses")

    course_map = {
        "Docker": "Docker for Beginners - Udemy",
        "Aws": "AWS Cloud Practitioner - AWS Skill Builder",
        "Microservices": "Spring Boot Microservices - Udemy",
        "Kubernetes": "Kubernetes Basics - Kubernetes.io",
        "React": "React - Scrimba",
        "Machine Learning": "Machine Learning by Andrew Ng - Coursera"
    }

    recommended = False

    for skill in missing:
        if skill in course_map:
            st.info(f"📚 {skill} → {course_map[skill]}")
            recommended = True

    if not recommended:
        st.success("Your resume already covers the detected job skills.")

    st.markdown("---")
        # ---------------- AI Resume Rewrite ---------------- #

    st.subheader("🤖 AI Resume Rewrite (Gemini)")

    if st.button("✨ Rewrite Resume with AI"):

        with st.spinner("Improving your resume..."):

            improved_resume = rewrite_resume_ai(resume_text)

        st.success("✅ Resume rewritten successfully!")

        st.text_area(
            "AI Improved Resume",
            improved_resume,
            height=350
        )

        st.download_button(
            "📄 Download Improved Resume",
            improved_resume,
            file_name="AI_Improved_Resume.txt",
            mime="text/plain"
        )

    # ---------------- PDF Report ---------------- #

    st.markdown("---")
    st.subheader("📄 ATS Analysis Report")

    report_path = generate_report(
        ats,
        match_score,
        skills,
        matched,
        missing,
        suggestions
    )

    with open(report_path, "rb") as pdf_file:

        st.download_button(
            "📥 Download ATS Report",
            pdf_file,
            file_name="ATS_Report.pdf",
            mime="application/pdf"
        )

    # ---------------- AI Cover Letter ---------------- #

    st.markdown("---")
    st.subheader("💌 AI Cover Letter Generator")

    name = st.text_input("👤 Your Name")

    job_role = st.text_input(
        "💼 Job Role",
        "Java Developer"
    )

    company = st.text_input(
        "🏢 Company Name"
    )

    if st.button("✨ Generate Cover Letter"):

        with st.spinner("Generating Cover Letter..."):

            cover_letter = generate_cover_letter_ai(
                name,
                job_role,
                company,
                resume_text
            )

        st.success("✅ Cover Letter Generated!")

        st.text_area(
            "Generated Cover Letter",
            cover_letter,
            height=350
        )

        st.download_button(
            "📄 Download Cover Letter",
            cover_letter,
            file_name="AI_Cover_Letter.txt",
            mime="text/plain"
        )

    # ---------------- AI Mock Interview ---------------- #

    st.markdown("---")
    st.subheader("🎤 AI Mock Interview")

    role = st.text_input(
        "Enter Job Role",
        "Java Developer",
        key="role_input"
    )

    if st.button("Generate Interview Questions"):

        with st.spinner("Generating Questions..."):

            questions = generate_interview_questions(role)

        st.success("✅ Interview Questions Ready!")

        st.text_area(
            "Interview Questions",
            questions,
            height=400
        )

        st.download_button(
            "📄 Download Questions",
            questions,
            file_name="Interview_Questions.txt",
            mime="text/plain"
        )

    st.markdown("---")
    st.success("🎉 AI Resume Analysis Completed Successfully!")
st.markdown("""
<div class="footer">

Made with ❤️ by <b>Shrutika Gadekar</b>

Python • Machine Learning • NLP • Streamlit

</div>
""", unsafe_allow_html=True)