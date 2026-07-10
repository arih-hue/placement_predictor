from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
RANDOM_STATE = 42
TEST_SIZE = 0.2
CLASSIFIER_PARAMS = {
    "n_estimators": 500,
    "learning_rate": 0.05,
    "min_child_weight": 3,
    "max_depth": 5,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "gamma": 0.2,
    "random_state": RANDOM_STATE
}
REGRESSOR_PARAMS = {
    "n_estimators": 500,
    "learning_rate": 0.05,
    "min_child_weight": 3,
    "max_depth": 5,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "gamma": 0.2,
    "random_state": RANDOM_STATE,
    "n_jobs": -1,
    "eval_metric": "rmse"
}
TARGET_CLASSIFICATION = "placement_status"
TARGET_REGRESSION = "salary_package_lpa"
DATA_PATH = BASE_DIR / "data" / "student_placement.csv"
CLASSIFIER_MODEL_PATH = BASE_DIR / "models" / "placement_model.pkl"
REGRESSOR_MODEL_PATH = BASE_DIR / "models" / "salary_model.pkl"
BRANCH_ENCODER_PATH = BASE_DIR / "models" / "branch_encoder.pkl"
TIER_ENCODER_PATH = BASE_DIR / "models" / "tier_encoder.pkl"
FEATURE_COLUMNS_PATH = BASE_DIR / "models" / "feature_columns.pkl"