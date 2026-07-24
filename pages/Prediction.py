import streamlit as st
import pandas as pd
from src.predict import predict
st.title("Placement Prediction")
st.write("Enter the student's details below.")
st.divider()
st.header("Academic Details")
col1, col2 = st.columns(2)
with col1:
    cgpa = st.slider(
        "CGPA",
        0.0,
        10.0,
        8.0,
        0.1
    )
    backlogs = st.number_input(
        "Backlogs",
        min_value=0,
        max_value=20,
        value=0
    )
with col2:
    branch = st.selectbox(
        "Branch",
        [
            "CSE",
            "IT",
            "ECE",
            "EEE",
            "Mechanical",
            "Civil"
        ]
    )
    college_tier = st.selectbox(
        "College Tier",
        [
            "Tier 1",
            "Tier 2",
            "Tier 3"
        ]
    )
st.divider()
st.header("Technical Skills")
st.subheader("Coding Skills")
st.caption("""
**Reference:**
- **90-100:** Built multiple full-stack or ML projects, comfortable with advanced concepts, can develop applications independently.
- **75-89:** Built a few good projects, strong understanding of programming fundamentals.
- **60-74:** Comfortable with DSA and programming basics, completed several coursework projects.
- **40-59:** Beginner to intermediate, knows one programming language and basic problem solving.
- **0-39:** Just started learning programming.
""")
coding_skills = st.slider("Coding Skills",0,100,70)
st.subheader("Data Structures & Algorithms")
st.caption("""
**Reference:**
- **90-100:** LeetCode 1800+ or Codeforces Specialist (1400+), solved 1000+ problems.
- **80-89:** LeetCode 1600-1800, solved 600-1000 problems.
- **65-79:** Solved 300-600 problems, comfortable with graphs, DP, trees.
- **50-64:** Solved 100-300 problems, knows common interview patterns.
- **0-49:** Less than 100 problems solved or still learning DSA basics.
""")
dsa_score = st.slider("DSA Score",0,100,70)
st.caption("""
**Reference:**
- **90-100:** Consistently scores above 90% in aptitude mock tests.
- **75-89:** Usually scores between 75-90%.
- **60-74:** Average aptitude performance.
- **40-59:** Needs improvement.
- **0-39:** Beginner.
""")
aptitude_score = st.slider("Aptitude Score",0,100,70)
st.caption("""
**Reference:**
- **90-100:** Confident speaker, presentations, leadership, fluent communication.
- **75-89:** Comfortable in interviews and group discussions.
- **60-74:** Can communicate ideas clearly but lacks confidence.
- **40-59:** Hesitates during interviews.
- **0-39:** Needs significant improvement.
""")
communication_skills = st.slider("Communication Skills",0,100,70)
st.caption("""
**Reference:**
- **90-100:** Built multiple ML projects, understands model selection, pipelines and deployment.
- **75-89:** Completed ML courses and built a few projects.
- **60-74:** Knows regression, classification and preprocessing.
- **40-59:** Basic understanding of supervised learning.
- **0-39:** New to ML.
""")
ml_knowledge = st.slider("Machine Learning Knowledge",0,100,50)
st.caption("""
**Reference:**
- **90-100:** Can design scalable systems, databases, caching and distributed services.
- **75-89:** Understands common system design concepts.
- **60-74:** Familiar with APIs, databases and application architecture.
- **40-59:** Beginner.
- **0-39:** No experience.
""")
system_design = st.slider("System Design",0,100,50)
st.divider()
st.header("Experience")
col1, col2 = st.columns(2)
with col1:
    internships = st.number_input("Internships",0,10,1)
    projects_count = st.number_input("Projects",0,20,2)
with col2:
    hackathons = st.number_input("Hackathons",0,20,1)
    open_source_contributions = st.number_input("Open Source Contributions",0,500,10)
st.divider()
if st.button("Predict Placement"):
    student = pd.DataFrame({
        "cgpa":[cgpa],
        "backlogs":[backlogs],
        "coding_skills":[coding_skills],
        "dsa_score":[dsa_score],
        "aptitude_score":[aptitude_score],
        "communication_skills":[communication_skills],
        "ml_knowledge":[ml_knowledge],
        "system_design":[system_design],
        "internships":[internships],
        "projects_count":[projects_count],
        "hackathons":[hackathons],
        "open_source_contributions":[open_source_contributions],
        "branch":[branch],
        "college_tier":[college_tier]
    })
    result = predict(student)
    st.divider()
    st.header("Prediction Result")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "Placement Status",
            result["placement_status"]
        )
    with col2:
        st.metric(
            "Placement Probability",
            f"{result['placement_probability']*100:.2f}%"
        )
    if result["placement_status"] == "Placed":
        st.success("Student is likely to get placed!")
        st.metric(
            "Expected Salary Package",
            f"{result['salary (LPA)']:.2f} LPA"
        )
    else:
        st.error("Student is unlikely to get placed.")