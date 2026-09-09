# Pandas Data Analytics Microservice

A modular backend API built with **FastAPI** and **Pandas** designed for sheet uploads (CSV/Excel), automated exploratory data analysis, and filtered query reporting.

## cheat sheet
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              PANDAS PRODUCTION CHEAT SHEET                                     │
├──────────────────┬───────────────────────────────────────────┬─────────────────────────────────┤
│ TASK             │ PANDAS CODE SNIPPET                       │ WHAT IT DOES                    │
├──────────────────┼───────────────────────────────────────────┼─────────────────────────────────┤
│ Read CSV         │ df = pd.read_csv("file.csv")              │ Parses CSV into DataFrame       │
│ Read Excel       │ df = pd.read_excel("file.xlsx")           │ Reads .xlsx or .xls             │
│ Dimensions       │ rows, cols = df.shape                     │ Tuple of (rows, cols)           │
│ Headers          │ cols = df.columns.tolist()                │ Extracts list of column names   │
│ Data Types       │ df.dtypes                                 │ Returns data type per column    │
│ Preview Data     │ df.head(5) / df.tail(5)                   │ Returns top / bottom 5 rows     │
│ Missing Count    │ df.isnull().sum()                         │ Checks missing cells per column │
│ Fill Missing     │ df_clean = df.fillna("")                  │ Prevents FastAPI JSON crashes   │
│ Drop Missing     │ df.dropna(subset=['Column'])              │ Removes rows missing 'Column'   │
│ Filter Exact     │ df[df['Country'] == 'Germany']            │ Filters rows matching value     │
│ Substring Search │ df[df['Col'].str.contains('x', na=False)] │ Searches keyword in text        │
│ Multi-Filter     │ df[(df['A'] > 1) & (df['B'] == 2)]        │ Multiple criteria filter        │
│ Group & Sum      │ df.groupby('A')['B'].sum().reset_index()  │ Aggregates metrics per category │
│ Sorting          │ df.sort_values(by='B', ascending=False)   │ Sorts descending                │
│ To API JSON      │ df.to_dict(orient="records")              │ Serializes DataFrame to JSON    │
└──────────────────┴───────────────────────────────────────────┴─────────────────────────────────┘

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
