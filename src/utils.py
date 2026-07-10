import joblib
import pandas as pd
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