import joblib
import numpy as np
from feature_eng import add_features
from config import (CLASSIFIER_MODEL_PATH,REGRESSOR_MODEL_PATH,BRANCH_ENCODER_PATH,TIER_ENCODER_PATH)

placement_model = joblib.load(CLASSIFIER_MODEL_PATH)
salary_model = joblib.load(REGRESSOR_MODEL_PATH)
branch_encoder = joblib.load(BRANCH_ENCODER_PATH)
tier_encoder = joblib.load(TIER_ENCODER_PATH)

def process_input(df):
    df = add_features(df)
    branch = branch_encoder.transform(df[['branch']])
    tier = tier_encoder.transform(df[['college_tier']])
    remaining = df.drop(columns=['branch', 'college_tier'])
    final_data = np.concatenate((remaining, branch, tier), axis=1)
    return final_data

def predict_placement(df):
    data = process_input(df)
    prediction = placement_model.predict(data)[0]
    probability = placement_model.predict_proba(data)[0][1]
    return prediction, probability

def predict_package(df):
    data = process_input(df)
    prediction = salary_model.predict(data)[0]
    prediction = np.expm1(prediction)
    return prediction

def predict(df):
    placed, probability = predict_placement(df)
    if placed == 0:
        return {"placement_status": "Not Placed","placement_probability": float(probability),"salary": 0}
    salary = predict_package(df)
    return {"placement_status": "Placed","placement_probability": float(probability),"salary (LPA)": round(float(salary),2)}