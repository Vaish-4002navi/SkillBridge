import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Career Database
# -------------------------------

career_skills = {
    "Data Analyst": ["Python", "SQL", "Excel", "Power BI", "Statistics"],
    "Data Scientist": ["Python", "SQL", "Machine Learning", "Statistics", "Pandas"],
    "Software Developer": ["Python", "Java", "DSA", "Git", "Problem Solving"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Git"],
    "Business Analyst": ["Excel", "SQL", "Power BI", "Communication", "Statistics"]
}

all_skills = [
    "Python", "SQL", "Excel", "Power BI", "Statistics",
    "Machine Learning", "Pandas", "Java", "DSA", "Git",
    "Problem Solving", "HTML", "CSS", "JavaScript",
    "React", "Communication"
]

# -------------------------------
# Page Settings
# -------------------------------

st.set_page_config(
    page_title="SkillBridge",
    page_icon="🎯",
    layout="wide"
)

# -------------------------------
# Header
# -------------------------------

st.title("🎯 SkillBridge")
st.subheader("Intelligent Skill Gap Analysis & Career Recommendation System")

st.markdown("---")

# -------------------------------
# User Input
# -------------------------------

career = st.selectbox(
    "Select Your Target Career",
    list(career_skills.keys())
)

skills = st.multiselect(
    "Select Your Current Skills",
    all_skills
)

# -------------------------------
# Analyze Button
# -------------------------------

if st.button("Analyze Skills"):

    required = career_skills[career]

    matched = []
    missing = []

    for skill in required:
        if skill in skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (len(matched) / len(required)) * 100

    # Readiness Score
    st.success(f"Readiness Score: {score:.0f}%")

    st.progress(int(score))

    # Status
    if score >= 80:
        st.success("Excellent! You are almost job-ready.")
    elif score >= 60:
        st.warning("Good progress. Learn the missing skills.")
    else:
        st.error("You need significant skill development.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Skills You Have")
        for skill in matched:
            st.write(skill)

    with col2:
        st.subheader("❌ Missing Skills")
        for skill in missing:
            st.write(skill)

    # Recommendations
    st.subheader("📚 Learning Recommendations")

    for skill in missing:
        st.write(f"➡ Learn {skill}")

    # Pie Chart
    st.subheader("📊 Skill Analysis Chart")

    labels = ["Completed", "Missing"]
    values = [len(matched), len(missing)]

    fig, ax = plt.subplots()

    ax.pie(
        values,
        labels=labels,
        autopct='%1.1f%%'
    )

    ax.set_title("Skill Readiness")

    st.pyplot(fig)

# -------------------------------
# Footer
# -------------------------------

st.markdown("---")
st.caption("Developed using Streamlit")
