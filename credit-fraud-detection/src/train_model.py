import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier

from utils.data_loader import load_raw_data
from utils.preprocessing import preprocess_data
from utils.feature_engineering import add_features
from utils.model_utils import save_model

df = load_raw_data("data/raw/transaction_data.csv")
df = add_features(df)
X, y, scaler = preprocess_data(df)

# Handle imbalance
X_res, y_res = SMOTE().fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2)

model = XGBClassifier(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.1,
    eval_metric='logloss'
)

model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))

save_model(model, "model/fraud_model.pkl")
