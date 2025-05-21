import os
import httpx # type: ignore

# Store Gemini 2.0 Flash API Key
from google import genai
from google.genai import types # type: ignore

from app.model.schemas import TestCaseModel

def test_scenarios_generation(
    file_bytes: bytes,
    file_mime_type: str,
):
    client = genai.Client(
        api_key = os.getenv("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash"

    prompt = (
        'Analyze the provided document and generate test scenarios.'
        ' where each item must be in the following format:'
        ' {"module": "module name", "requirement_id": "[optional]", "test_scenario_id": "[TS_01, TS_02]", "description": ["description 1.", "description 2."]}'
        ' Focus on available modules and their requirements.' 
        ' Ensure keys are lowercase.'
    )

    contents = [
        types.Part(inline_data=types.Blob(mime_type=file_mime_type, data=file_bytes)),
        types.Part(text=prompt)
    ]

    content_config = {
        "response_mime_type": "application/json",
        "response_schema": list[TestCaseModel]
    }

    response = client.models.generate_content(
        model = model,
        contents = contents,
        config = content_config,
    )

    # Use the response as a JSON string.
    return response.text