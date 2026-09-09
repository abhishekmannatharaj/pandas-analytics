import io
import pandas as pd
from typing import Optional, List, Dict, Any


def load_dataframe_from_bytes(file_contents: bytes, filename: str) -> pd.DataFrame:
    """Helper function to load bytes into a Pandas DataFrame safely."""
    if filename.endswith(".csv"):
        return pd.read_csv(io.BytesIO(file_contents))
    elif filename.endswith((".xlsx", ".xls")):
        return pd.read_excel(io.BytesIO(file_contents))
    else:
        raise ValueError("Unsupported format. Please upload CSV or Excel files (.xlsx, .xls).")


def get_dataset_summary(file_contents: bytes, filename: str) -> dict:
    """Computes high-level dataset metrics, headers, and head sample."""
    df = load_dataframe_from_bytes(file_contents, filename)
    df_clean = df.fillna("")

    return {
        "filename": filename,
        "total_rows": int(df.shape[0]),
        "total_columns": int(df.shape[1]),
        "columns": list(df.columns),
        "sample_data": df_clean.head(5).to_dict(orient="records"),
    }


def filter_dataset(
    file_contents: bytes,
    filename: str,
    column_name: str,
    search_value: str,
    limit: int = 50
) -> Dict[str, Any]:
    """Filters dataset rows matching a keyword in a specified column."""
    df = load_dataframe_from_bytes(file_contents, filename)

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found. Available: {list(df.columns)}")

    # Case-insensitive substring match
    matched_df = df[
        df[column_name].astype(str).str.contains(search_value, case=False, na=False)
    ]
    matched_df_clean = matched_df.fillna("")

    return {
        "filtered_by_column": column_name,
        "search_query": search_value,
        "matched_rows_count": int(matched_df.shape[0]),
        "records": matched_df_clean.head(limit).to_dict(orient="records"),
    }