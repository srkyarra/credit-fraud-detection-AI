import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df: pd.DataFrame):
    df = df.copy()
    df = df.dropna()

    scaler = StandardScaler()
    df['amount_scaled'] = scaler.fit_transform(df[['Amount']])

    X = df.drop('Class', axis=1)
    y = df['Class']

    return X, y, scaler
