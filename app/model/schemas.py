from pydantic import BaseModel # type: ignore
from typing import Optional, List

class TestCaseModel(BaseModel):
    module: str
    requirement_id: List[str]
    test_scenario_id: List[str]
    description: List[str] 