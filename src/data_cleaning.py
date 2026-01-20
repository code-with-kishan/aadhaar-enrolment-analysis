def clean_dataframe(df):
    """
    Standardize column names and remove duplicate rows.
    """
    if df is None or df.empty:
        return df

    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df = df.drop_duplicates()
    return df
