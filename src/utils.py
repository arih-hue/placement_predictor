import joblib
import pandas as pd
import streamlit as st

from src.config import (
    CLASSIFIER_MODEL_PATH,
    REGRESSOR_MODEL_PATH,
    BRANCH_ENCODER_PATH,
    TIER_ENCODER_PATH,
)

def load_dataset(path):
    return pd.read_csv(path)

def save_model(model, path):
    joblib.dump(model, path)

def load_model(path):
    return joblib.load(path)

def save_object(obj, path):
    joblib.dump(obj, path)

def load_object(path):
    return joblib.load(path)

@st.cache_resource(show_spinner=False)
def load_models():
    placement_model = joblib.load(CLASSIFIER_MODEL_PATH)
    salary_model = joblib.load(REGRESSOR_MODEL_PATH)
    branch_encoder = joblib.load(BRANCH_ENCODER_PATH)
    tier_encoder = joblib.load(TIER_ENCODER_PATH)
    return placement_model, salary_model, branch_encoder, tier_encoder