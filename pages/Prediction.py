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
coding_skills = st.slider(
    "Coding Skills",
    0,
    100,
    70
)
dsa_score = st.slider(
    "DSA Score",
    0,
    100,
    70
)
aptitude_score = st.slider(
    "Aptitude Score",
    0,
    100,
    70
)
communication_skills = st.slider(
    "Communication Skills",
    0,
    100,
    70
)
ml_knowledge = st.slider(
    "Machine Learning Knowledge",
    0,
    100,
    50
)
system_design = st.slider(
    "System Design",
    0,
    100,
    50
)
st.divider()
st.header("Experience")
col1, col2 = st.columns(2)
with col1:
    internships = st.number_input(
        "Internships",
        0,
        10,
        1
    )
    projects_count = st.number_input(
        "Projects",
        0,
        20,
        2
    )
with col2:
    hackathons = st.number_input(
        "Hackathons",
        0,
        20,
        1
    )
    open_source_contributions = st.number_input(
        "Open Source Contributions",
        0,
        500,
        10
    )
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
            f"{result['salary']:.2f} LPA"
        )
    else:
        st.error("Student is unlikely to get placed.")