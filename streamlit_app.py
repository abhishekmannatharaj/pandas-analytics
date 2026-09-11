from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")
st.title("📊 Sales Data Analytics Dashboard")
st.caption("Interactive data explorer built with Streamlit and Pandas.")

# Dataset Path
DEFAULT_DATA_PATH = Path("data/raw/Sales.csv")

@st.cache_data
def load_data(file_path_or_buffer):
    """Loads and caches the dataset to optimize re-renders."""
    return pd.read_csv(file_path_or_buffer)

# 1. File Upload or Default Fallback
uploaded_file = st.file_uploader(
    "Upload a CSV dataset (optional):", type=["csv"]
)
df = None
if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.success(f"Loaded uploaded file: `{uploaded_file.name}`")
elif DEFAULT_DATA_PATH.exists():
    df = load_data(DEFAULT_DATA_PATH)
    st.info(f"Loaded default dataset from `{DEFAULT_DATA_PATH}`")
else:
    st.warning("No data found. Upload a CSV file to proceed.")

if df is not None:
    # 2. High-Level Metrics (KPI Cards)
    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", f"{df.shape[0]:,}")
    col2.metric("Total Attributes", df.shape[1])
    col3.metric(
        "Numeric Columns", len(df.select_dtypes(include="number").columns)
    )

    st.divider()
    # 3. Interactive Data Filtering
    st.subheader("Filter Records")
    col_filter, col_query = st.columns([1, 2])

    with col_filter:
        selected_column = st.selectbox(
            "Select column to search:", options=df.columns.tolist()
        )

    with col_query:
        search_query = st.text_input("Enter search query or substring:")

    if search_query:
        filtered_df = df[
            df[selected_column]
            .astype(str)
            .str.contains(search_query, case=False, na=False)
        ]
        st.write(f"Matched **{len(filtered_df):,}** records:")
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.subheader("Dataset Preview (First 10 Rows)")
        st.dataframe(df.head(10), use_container_width=True)

    st.divider()
    # 4. Quick Distribution Visualizer
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        st.subheader("Visual Distribution")
        chart_col = st.selectbox(
            "Select numerical column to plot:", options=numeric_cols
        )
        st.bar_chart(df[chart_col].head(50))