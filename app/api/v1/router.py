from fastapi import APIRouter, File, HTTPException, Query, UploadFile, status
from app.api.v1.schemas import DatasetSummaryResponse
from app.services.analyze_data import get_dataset_summary, filter_dataset

router = APIRouter(prefix="/analytics", tags=["Data Analytics"])


@router.post(
    "/upload-summary",
    response_model=DatasetSummaryResponse,
    status_code=status.HTTP_200_OK,
)
async def upload_file_summary(file: UploadFile = File(...)):
    if not (
        file.filename.endswith(".csv")
        or file.filename.endswith(".xlsx")
        or file.filename.endswith(".xls")
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only CSV and Excel sheets (.xlsx, .xls) are supported.",
        )

    try:
        contents = await file.read()
        return get_dataset_summary(contents, file.filename)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error reading dataset: {str(exc)}",
        )


@router.post("/filter", status_code=status.HTTP_200_OK)
async def filter_file_data(
    file: UploadFile = File(...),
    column_name: str = Query(..., description="Target column to search within"),
    search_value: str = Query(..., description="Value or substring to match"),
    limit: int = Query(50, ge=1, le=500, description="Max rows returned"),
):
    try:
        contents = await file.read()
        return filter_dataset(contents, file.filename, column_name, search_value, limit)
    except ValueError as val_err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(val_err))
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error filtering dataset: {str(exc)}",
        )