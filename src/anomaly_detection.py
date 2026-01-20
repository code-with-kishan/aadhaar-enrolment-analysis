from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df, value_col):
    """
    Detect anomalies using Isolation Forest.
    """
    if df is None or df.empty or value_col not in df.columns:
        return df

    X = pd.to_numeric(df[value_col], errors="coerce").fillna(0)
    X = X.values.reshape(-1, 1)

    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,
        random_state=42
    )

    df["anomaly_flag"] = model.fit_predict(X)
    return df
