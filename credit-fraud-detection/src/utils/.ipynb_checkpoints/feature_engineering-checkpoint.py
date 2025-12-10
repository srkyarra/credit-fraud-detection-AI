import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['hour'] = df['Time'] % 24
    df['amount_squared'] = df['Amount'] ** 2
    return df
