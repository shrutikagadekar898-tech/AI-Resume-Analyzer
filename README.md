# 🤖 AI Resume Analyzer with Gemini AI

An AI-powered Resume Analyzer built using **Python, Streamlit, NLP, Machine Learning, and Google Gemini AI**.

It helps users analyze their resume, calculate ATS score, compare it with a Job Description, generate AI-powered resume improvements, create cover letters, and prepare for interviews.

---

## 📸 Screenshots

> Add screenshots inside the `assets` folder.

Example:

```
assets/
│── dashboard.png
│── ats_score.png
│── resume_match.png
│── cover_letter.png
│── interview.png
```

---

## ✨ Features

- 📄 Upload Resume (PDF)
- 🔍 Resume Text Extraction
- ⭐ ATS Score Calculation
- 🎯 Resume vs Job Description Match
- 🛠 Skill Extraction
- ✅ Matching Skills
- ❌ Missing Skills
- 💡 Resume Improvement Suggestions
- 📊 Interactive Dashboard
- 📈 Charts & Visualizations
- 📥 Download ATS Analysis PDF
- 🤖 AI Resume Summary
- ✨ AI Resume Rewrite (Google Gemini)
- 📄 AI Cover Letter Generator
- 🎤 AI Mock Interview Questions

---

## 🛠 Tech Stack

### Frontend
- Streamlit
- HTML
- CSS

### Backend
- Python

### AI / Machine Learning
- Google Gemini AI
- NLP
- TF-IDF
- Cosine Similarity

### Libraries
- Streamlit
- PyPDF2
- Pandas
- Scikit-learn
- Plotly
- ReportLab
- Google Generative AI
- python-dotenv

---

## 📂 Project Structure

```
AIResumeAnalyzer/
│
├── assets/
├── reports/
├── utils/
│   ├── pdf_reader.py
│   ├── skill_extractor.py
│   ├── matcher.py
│   ├── ats_score.py
│   ├── report_generator.py
│   ├── ai_summary.py
│   ├── gemini_rewriter.py
│   ├── gemini_cover_letter.py
│   └── gemini_interview.py
│
├── app.py
├── requirements.txt
├── skills.csv
├── courses.csv
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
```

Go to the project folder

```bash
cd AI-Resume-Analyzer
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run the Project

```bash
streamlit run app.py
```

---

## 🔑 Environment Variables

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## 📊 Workflow

```
Resume PDF
      │
      ▼
Extract Resume Text
      │
      ▼
Skill Extraction
      │
      ▼
ATS Score
      │
      ▼
Resume vs JD Match
      │
      ▼
Missing Skills
      │
      ▼
AI Resume Rewrite
      │
      ▼
AI Cover Letter
      │
      ▼
Mock Interview
      │
      ▼
PDF Report
```

---

## 🚀 Future Enhancements

- AI Voice Interview
- Resume Ranking
- Resume Templates
- Job Recommendation System
- Multi-language Resume Analysis

---

## 👩‍💻 Author

**Shrutika Gadekar**

GitHub:
https://github.com/shrutikagadekar898-tech

---

## ⭐ If you like this project

Please give this repository a ⭐ on GitHub.
