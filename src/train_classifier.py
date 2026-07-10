from xgboost import XGBClassifier
from evaluate import evaluate_classifier
from feature_eng import add_features
from processing import preprocess_classifier
from utils import save_model
from utils import load_dataset
from config import *

df = load_dataset(DATA_PATH)
df = add_features(df)
x_train, x_test, y_train, y_test, ohe_branch, lbl_tier = preprocess_classifier(df)
model = XGBClassifier(**CLASSIFIER_PARAMS)
model.fit(x_train, y_train)
evaluate_classifier(model,x_train,x_test,y_train,y_test)
save_model(model, CLASSIFIER_MODEL_PATH)
save_model(ohe_branch, BRANCH_ENCODER_PATH)
save_model(lbl_tier, TIER_ENCODER_PATH)
print("Placement model save successfull")