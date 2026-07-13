import streamlit as st
st.set_page_config(
    page_title="Student Placement Predictor",
    layout="wide"
)
st.title("Student Placement & Salary Prediction")
st.markdown("---")
st.write("""
Welcome to the **Student Placement & Salary Prediction Dashboard**.

This project predicts

- Placement Status
- Expected Salary Package

using Machine Learning.

Navigate using the **sidebar**.
""")
st.markdown("---")
st.header("About the Project")
st.write("""
The objective of this project is to predict whether a student will be placed during campus placements and estimate the salary package offered.

The prediction is based on various academic, technical, and extracurricular features collected from students.
""")
st.header("Models Used")
col1, col2 = st.columns(2)
with col1:
    st.success("XGBoost Classifier")
    st.write("""
Predicts whether the student will be placed or not.
""")
with col2:
    st.success("XGBoost Regressor")
    st.write("""
Predicts the expected salary package.
""")
st.markdown("---")
st.header("Feature Engineering")
st.write("""
Additional features created during preprocessing:

- Technical Score
- Academic Score
- Experience Score
- DSA × Coding Score
- Resume Strength
""")
st.markdown("---")
st.header("Features Used")
left, right = st.columns(2)
with left:
    st.write("""
### Academic

- CGPA
- Backlogs
- College Tier
- Branch

### Technical

- Coding Skills
- DSA Score
- ML Knowledge
- System Design
""")
with right:
    st.write("""
### Experience

- Internships
- Projects
- Hackathons
- Open Source Contributions

### Soft Skills

- Aptitude Score
- Communication Skills
""")
st.markdown("---")
st.header("How to Use")
st.write("""
1. Open **Dashboard** to view dataset statistics.

2. Open **EDA** to explore the dataset.

3. Open **Model Performance** to see model evaluation.

4. Open **Prediction** to predict placement and salary.
""")
st.info("Use the sidebar to navigate through different pages.")