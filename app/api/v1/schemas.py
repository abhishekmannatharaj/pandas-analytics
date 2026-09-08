from typing import Any, Dict, List
from pydantic import BaseModel


class DatasetSummaryResponse(BaseModel):
    filename: str
    total_rows: int
    total_columns: int
    columns: List[str]
    sample_data: List[Dict[str, Any]]