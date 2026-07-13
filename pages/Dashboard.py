import streamlit as st
import pandas as pd
st.title("Dashboard")
st.write("Dataset Overview and Placement Statistics")
st.divider()
df = pd.read_csv("data/student_placement.csv")
total_students = len(df)
placed_students = len(df[df["placement_status"] == 1])
not_placed = len(df[df["placement_status"] == 0])
placement_rate = (placed_students / total_students) * 100
average_salary = df[df["placement_status"] == 1]["salary_package_lpa"].mean()
median_salary = df[df["placement_status"] == 1]["salary_package_lpa"].median()
highest_salary = df["salary_package_lpa"].max()
st.subheader("Dataset Statistics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Students", total_students)
with col2:
    st.metric("Placed Students", placed_students)
with col3:
    st.metric("Not Placed", not_placed)
st.write("")
col4, col5, col6 = st.columns(3)
with col4:
    st.metric("Placement Rate", f"{placement_rate:.2f}%")
with col5:
    st.metric("Average Salary", f"{average_salary:.2f} LPA")
with col6:
    st.metric("Highest Salary", f"{highest_salary:.2f} LPA")
st.divider()
st.subheader("Placement Distribution")
st.image(
    "assets/placement_dis.png",
    use_container_width=True
)
st.divider()
st.subheader("CGPA Distribution")
st.image(
    "assets/cgpa_dis.png",
    use_container_width=True
)
st.divider()
st.subheader("Placement Rate by Branch")
st.image(
    "assets/branch_placed.png",
    use_container_width=True
)
st.divider()
st.subheader("Placement Rate by College Tier")
st.image(
    "assets/tier_placed.png",
    use_container_width=True
)
st.divider()
st.subheader("Average Salary by Branch")
st.image(
    "assets/branch_pkg.png",
    use_container_width=True
)
st.divider()
st.subheader("Average Salary by College Tier")
st.image(
    "assets/tier_pkg.png",
    use_container_width=True
)