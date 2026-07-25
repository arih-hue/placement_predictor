import numpy as np

from src.feature_eng import add_features
from src.utils import load_models

def process_input(df, branch_encoder, tier_encoder):
    df=add_features(df)
    branch=branch_encoder.transform(df[["branch"]])
    tier=tier_encoder.transform(df[["college_tier"]])
    remaining=df.drop(columns=["branch", "college_tier"])
    final_data= np.concatenate((remaining, branch, tier), axis=1)
    return final_data

def predict(df):
    placement_model, salary_model, branch_encoder, tier_encoder = load_models()
    data=process_input(df, branch_encoder, tier_encoder)

    probability =placement_model.predict_proba(data)[0][1]
    placed=placement_model.predict(data)[0]

    if placed == 0:
        return {
            "placement_status": "Not Placed",
            "placement_probability": float(probability),
            "salary (LPA)": 0,
        }

    salary = np.expm1(salary_model.predict(data)[0])

    return {
        "placement_status": "Placed",
        "placement_probability": float(probability),
        "salary (LPA)": round(float(salary), 2),
    }