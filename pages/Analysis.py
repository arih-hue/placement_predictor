import streamlit as st
st.title("Exploratory Data Analysis")
st.write("Visual analysis of the student placement dataset.")
st.divider()
st.subheader("Placement Rate by CGPA")
st.write("""
This graph shows how placement rate changes across different CGPA ranges.
""")
st.image(
    "assets/cg_vs_placement.png",
    use_container_width=True
)
st.divider()
st.subheader("Coding Skills vs Salary Package")
st.write("""
Students with stronger coding skills generally receive higher salary packages.
""")
st.image(
    "assets/cs_vs_pkg.png",
    use_container_width=True
)
st.divider()
st.subheader("DSA Score vs Salary Package")
st.write("""
Higher DSA scores are associated with better salary offers.
""")
st.image(
    "assets/dsa_vs_pkg.png",
    use_container_width=True
)
st.divider()
st.subheader("Communication Skills vs Salary")
st.write("""
Communication skills also contribute to higher salary packages.
""")
st.image(
    "assets/com_vs_pkg.png",
    use_container_width=True
)
st.divider()
st.subheader("Correlation Heatmap")
st.write("""
The heatmap shows the correlation between different numerical features.
""")
st.image(
    "assets/ultimate_corr.png",
    use_container_width=True
)