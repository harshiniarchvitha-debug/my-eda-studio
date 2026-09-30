from pathlib import Path
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Loads a CSV or Parquet file into a Pandas DataFrame."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if path.suffix == ".csv":
        return pd.read_csv(path)
    elif path.suffix in [".parquet", ".pq"]:
        return pd.read_parquet(path)
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}. Use .csv or .parquet")