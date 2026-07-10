from xgboost import XGBRegressor
from evaluate import evaluate_regressor
from feature_eng import add_features
from processing import preprocess_regressor
from utils import load_dataset
from utils import save_model
from config import *

df = load_dataset(DATA_PATH)
df = add_features(df)
x_train, x_test, y_train, y_test, ohe_branch, lbl_tier, func_trans = preprocess_regressor(df)
model = XGBRegressor(**REGRESSOR_PARAMS)
model.fit(x_train, y_train)
evaluate_regressor(model,x_train,x_test,y_train,y_test)
save_model(model, REGRESSOR_MODEL_PATH)
print("Salary model save successful")