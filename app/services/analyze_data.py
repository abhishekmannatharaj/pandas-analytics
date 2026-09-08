import io
import pandas as pd


def get_dataset_summary(file_contents: bytes, filename: str) -> dict:
    # Handle CSV or Excel formats
    if filename.endswith(".csv"):
        df = pd.read_csv(io.BytesIO(file_contents))
    elif filename.endswith((".xlsx", ".xls")):
        df = pd.read_excel(io.BytesIO(file_contents))
    else:
        raise ValueError("Unsupported file format. Please upload CSV or Excel.")

    # Clean missing values for JSON serialization
    df_clean = df.fillna("")

    return {
        "filename": filename,
        "total_rows": int(df.shape[0]),
        "total_columns": int(df.shape[1]),
        "columns": list(df.columns),
        "sample_data": df_clean.head(5).to_dict(orient="records"),
    }