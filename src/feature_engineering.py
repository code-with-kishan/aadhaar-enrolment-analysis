import pandas as pd

def add_time_features(df, date_col="date"):
    """
    Add year and month columns from a date field.
    """
    if df is None or df.empty:
        return df

    if date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
        df["year"] = df[date_col].dt.year
        df["month"] = df[date_col].dt.month

    return df


def add_total_enrolments(df):
    """
    Compute total enrolments from age-group columns if present.
    """
    if df is None or df.empty:
        return df

    age_columns = ["age_0_5", "age_5_17", "age_18_greater"]
    available = [c for c in age_columns if c in df.columns]

    if available:
        df[available] = df[available].apply(
            pd.to_numeric, errors="coerce"
        ).fillna(0)
        df["total_enrolments"] = df[available].sum(axis=1)

    return df
