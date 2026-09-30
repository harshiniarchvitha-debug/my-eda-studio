import pandas as pd

def assess_quality(df: pd.DataFrame) -> dict:
    """Inspects dataset health: missing values, duplicate rows, data types."""
    total_rows = len(df)
    null_counts = df.isnull().sum()
    
    missing_summary = [
        {
            "column": col,
            "missing_count": int(cnt),
            "missing_pct": round((cnt / total_rows) * 100, 2)
        }
        for col, cnt in null_counts.items() if cnt > 0
    ]
    
    return {
        "total_rows": total_rows,
        "total_columns": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_summary": missing_summary,
        "data_types": {col: str(dtype) for col, dtype in df.dtypes.items()}
    }