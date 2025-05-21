from fastapi import APIRouter, File, UploadFile, HTTPException # type: ignore
import tempfile
import os

from app.services.llm_inference import test_scenarios_generation
from app.services.json_to_csv import json_to_csv
from app.core.logger import logger

router = APIRouter()

RESULT_DIR = os.path.join("app", "result")
os.makedirs(RESULT_DIR, exist_ok=True)

@router.post("/automation-test-scenario")
async def create_automation_test_scenario(
    test_cases_file: UploadFile = File(...)
):
    """
    Create test automation scenario from the provided document
    """
    try:
        logger.info(f"Received file: {test_cases_file.filename}")

        file_bytes = await test_cases_file.read()
        file_mime_type = test_cases_file.content_type

        logger.info(f"File MIME type: {file_mime_type}")

        # Create temp directory to store uploaded files
        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = os.path.join(temp_dir, test_cases_file.filename)

            with open(image_path, "wb") as buffer:
                buffer.write(file_bytes)

            test_case = test_scenarios_generation(
                file_bytes=file_bytes,
                file_mime_type=file_mime_type
            )

            base_name, _ = os.path.splitext(test_cases_file.filename)
            output_csv_path = os.path.join(RESULT_DIR, f"{base_name}.csv")

            json_to_csv(test_case, output_csv_path)

            logger.info(f"Test case conversion successful. Result saved at: {output_csv_path}")

            return {
                "conversion": "success",
                "file_name": test_cases_file.filename
            } 
    
    except Exception as e:
        logger.error(f"Error processing file {test_cases_file.filename}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error processing test cases: {str(e)}")
    
    