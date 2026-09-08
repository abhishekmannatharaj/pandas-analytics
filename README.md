# Pandas Data Analytics Microservice

A modular backend API built with **FastAPI** and **Pandas** designed for sheet uploads (CSV/Excel), automated exploratory data analysis, and filtered query reporting.

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