from sklearn.calibration import CalibratedClassifierCV
from xgboost import XGBClassifier
from feature_eng import add_features
from processing import preprocess_classifier
from utils import save_model
from utils import load_dataset
from config import *
df = load_dataset(DATA_PATH)
df = add_features(df)
x_train, x_test, y_train, y_test, ohe_branch, lbl_tier = preprocess_classifier(df)
base_model = XGBClassifier(**CLASSIFIER_PARAMS)
model = CalibratedClassifierCV(estimator=base_model,method="sigmoid",cv=5)
model.fit(x_train, y_train)
save_model(model, CLASSIFIER_MODEL_PATH)
save_model(ohe_branch, BRANCH_ENCODER_PATH)
save_model(lbl_tier, TIER_ENCODER_PATH)
print("Placement model saved successfully")