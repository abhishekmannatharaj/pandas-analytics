from fastapi import APIRouter, File, HTTPException, UploadFile, status
from app.api.v1.schemas import DatasetSummaryResponse
from app.services.analyze_data import get_dataset_summary

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
        summary = get_dataset_summary(contents, file.filename)
        return summary
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error analyzing dataset: {str(exc)}",
        )