def yearly_aggregation(df, value_col):
    """
    Aggregate numeric column by year.
    """
    if df is None or df.empty:
        return None

    if "year" not in df.columns or value_col not in df.columns:
        return None

    return (
        df.groupby("year")[value_col]
        .sum()
        .reset_index()
    )


def statewise_aggregation(df, value_col):
    """
    Aggregate numeric column by state.
    """
    if df is None or df.empty:
        return None

    if "state" not in df.columns or value_col not in df.columns:
        return None

    return (
        df.groupby("state")[value_col]
        .sum()
        .reset_index()
    )
