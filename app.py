import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Career Database
# -------------------------------

career_skills = {
   "Data Analyst": ["Python", "SQL", "Excel", "Power BI", "Tableau"],
    "Data Scientist": ["Python", "SQL", "ML Libraries", "Pandas", "PyTorch", "Scikit-Learn", "TensorFlow", "Snowflake", "Apache Spark"],
    "Software Developer": ["Python", "Java", "C++", "C#", "Go", "Git", "Docker", "Kubernetes", "CI/CD"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js", "Angular", "Git", "REST APIs"],
    "Business Analyst": ["Excel", "SQL", "Power BI", "Jira", "Confluence", "Microsoft Visio", "Miro"],
    "Data Engineer": ["Python", "SQL", "Java", "Scala", "Apache Spark", "Airflow", "dbt", "Snowflake", "BigQuery"],
    "DevOps Engineer": ["Bash", "Python", "Go", "YAML", "AWS/Azure/GCP", "Docker", "Kubernetes", "Terraform", "GitHub Actions", "CI/CD"],
    "Cybersecurity Analyst": ["Python", "Bash", "PowerShell", "Wireshark", "Splunk", "Kali Linux", "Firewalls", "Metasploit"],
    "Product Manager": ["Jira", "Productboard", "Confluence", "Amplitude", "Miro"],
    "UX/UI Designer": ["HTML/CSS Basics", "Figma", "Adobe XD", "Sketch", "InVision"],
    "QA Automation Engineer": ["Python", "Java", "JavaScript", "Selenium", "Cypress", "Playwright", "Postman", "Jenkins"],
    "AI / ML Engineer": ["Python", "C++", "PyTorch", "TensorFlow", "MLflow", "Docker", "CUDA"]
}

skill_categories ={
    "💻 Programming Languages": ["None","Python", "Java", "C++", "C#", "Go", "JavaScript", "SQL", "Scala", "Bash", "PowerShell","Other"],
    "📊 Data & Analytics": ["None","Excel", "Power BI", "Tableau", "Pandas", "Apache Spark", "Snowflake", "BigQuery", "dbt","Other"],
    "🤖 AI / Machine Learning": ["None","ML Libraries", "PyTorch", "TensorFlow", "Scikit-Learn", "MLflow", "CUDA","Other"],
    "🌐 Web Development": ["None","HTML", "CSS", "React", "Node.js", "Angular", "REST APIs","Other"],
    "☁️ Cloud & DevOps": ["None","Docker", "Kubernetes", "Terraform", "GitHub Actions", "AWS/Azure/GCP", "CI/CD", "Airflow", "YAML","Other"],
    "🛡 Cybersecurity": ["None","Wireshark", "Splunk", "Kali Linux", "Firewalls", "Metasploit","Other"],
    "🧪 Testing": ["None","Selenium", "Cypress", "Playwright", "Postman", "Jenkins","Other"],
    "🎨 UI / UX Design": ["None","HTML/CSS Basics", "Figma", "Adobe XD", "Sketch", "InVision","Other"],
    "📋 Project Management": ["None","Jira", "Confluence", "Miro", "Productboard", "Amplitude", "Microsoft Visio","Other"]
}



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

st.subheader("🛠 Select Your Current Skills")

skills = []

for category, category_skills in skill_categories.items():
    with st.expander(category):
        selected = st.multiselect(
            "Choose skills",
            category_skills,
            key=category
        )
        skills.extend(selected)




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
st.caption("Developed by Vaishnavi.T | github:[Vaish-4002navi](https://github.com/Vaish-4002navi)")
