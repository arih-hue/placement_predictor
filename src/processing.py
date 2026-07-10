import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import FunctionTransformer

func_trans = FunctionTransformer(np.log1p)

def preprocess_classifier(df):
    x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=['placement_status', 'salary_package_lpa']),df['placement_status'],test_size=0.2,random_state=42,stratify=df['placement_status'])
    ohe_branch = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    lbl_tier = OrdinalEncoder(categories=[['Tier 3', 'Tier 2', 'Tier 1']])
    x_train_branch = ohe_branch.fit_transform(x_train[['branch']])
    x_train_tier = lbl_tier.fit_transform(x_train[['college_tier']])
    x_test_branch = ohe_branch.transform(x_test[['branch']])
    x_test_tier = lbl_tier.transform(x_test[['college_tier']])
    x_train_rem = x_train.drop(columns=['branch', 'college_tier'])
    x_test_rem = x_test.drop(columns=['branch', 'college_tier'])
    x_train = np.concatenate((x_train_rem, x_train_branch, x_train_tier), axis=1)
    x_test = np.concatenate((x_test_rem, x_test_branch, x_test_tier), axis=1)
    return x_train, x_test, y_train, y_test, ohe_branch, lbl_tier

def preprocess_regressor(df):
    df = df[df['placement_status'] == 1].copy()
    df['salary_package_lpa'] = func_trans.fit_transform(df[['salary_package_lpa']])
    x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=['placement_status', 'salary_package_lpa']),df['salary_package_lpa'],test_size=0.2,random_state=42)
    ohe_branch = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    lbl_tier = OrdinalEncoder(categories=[['Tier 3', 'Tier 2', 'Tier 1']])
    x_train_branch = ohe_branch.fit_transform(x_train[['branch']])
    x_train_tier = lbl_tier.fit_transform(x_train[['college_tier']])
    x_test_branch = ohe_branch.transform(x_test[['branch']])
    x_test_tier = lbl_tier.transform(x_test[['college_tier']])
    x_train_rem = x_train.drop(columns=['branch', 'college_tier'])
    x_test_rem = x_test.drop(columns=['branch', 'college_tier'])
    x_train = np.concatenate((x_train_rem, x_train_branch, x_train_tier), axis=1)
    x_test = np.concatenate((x_test_rem, x_test_branch, x_test_tier), axis=1)
    return x_train, x_test, y_train, y_test, ohe_branch, lbl_tier, func_trans