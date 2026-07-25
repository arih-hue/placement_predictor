import pandas as pd
import streamlit as st
@st.cache_data(ttl=3600, show_spinner=False)
def load_data():
    return pd.read_csv("data/student_placement.csv")