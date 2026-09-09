# Pandas Data Analytics Microservice

A modular backend API built with **FastAPI** and **Pandas** designed for sheet uploads (CSV/Excel), automated exploratory data analysis, and filtered query reporting.

## cheat sheet
# Pandas Production Cheat Sheet

| Task | Pandas Code Snippet | What It Does |
| :--- | :--- | :--- |
| **Read CSV** | `df = pd.read_csv("file.csv")` | Parses CSV file into a DataFrame |
| **Read Excel** | `df = pd.read_excel("file.xlsx")` | Reads `.xlsx` or `.xls` files (requires `openpyxl`) |
| **Dimensions** | `rows, cols = df.shape` | Returns `(total_rows, total_cols)` count |
| **Column Names** | `cols = df.columns.tolist()` | Extracts list of all column headers |
| **Data Types** | `df.dtypes` | Shows the data type of each column |
| **Preview Data** | `df.head(5)` / `df.tail(5)` | Returns top / bottom 5 rows |
| **Missing Values** | `df.isnull().sum()` | Total missing (`NaN`) cells per column |
| **Fill Missing** | `df_clean = df.fillna("")` | Replaces `NaN` to prevent JSON API errors |
| **Drop Missing** | `df.dropna(subset=['Col'])` | Drops rows where `'Col'` is null |
| **Exact Filter** | `df[df['Country'] == 'Germany']` | Filters rows matching value |
| **Substring Search** | `df[df['Col'].str.contains('text', na=False)]` | Case-insensitive substring match |
| **Multi-Filter** | `df[(df['A'] > 1) & (df['B'] == 2)]` | Combines conditions with `&` (AND) or `\|` (OR) |
| **Group & Sum** | `df.groupby('Country')['Revenue'].sum().reset_index()` | Aggregates numerical totals by category |
| **Sorting** | `df.sort_values(by='Revenue', ascending=False)` | Sorts records in descending order |
| **To JSON Dict** | `df.to_dict(orient="records")` | Converts DataFrame to list of dicts for FastAPI |

## Dataset
* **Target Dataset:** Europe Bike Store Sales

## Project Architecture
```text
pandas-analytics/
├── app/
│   ├── api/v1/          # Endpoints and schemas
│   ├── services/        # Pure Pandas analysis logic
│   └── main.py          # FastAPI application entrypoint
├── data/
│   ├── raw/             # Source CSV/Excel files (git-ignored)
│   └── processed/       # Cleaned exports
├── requirements.txt
└── README.md
