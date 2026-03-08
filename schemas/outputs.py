from pydantic import BaseModel, Field
from typing import Literal

class SegmentResult(BaseModel):
    segment_id: str
    start_pt_id: str
    end_pt_id: str
    measured_slope: float = Field(..., description="The calculated slope percentage")
    status: Literal["PASS", "WARN", "FAIL"] = Field(..., description="Strict compliance status")
    exception_note: str | None = Field(default=None, description="Required if status is FAIL but approved by QA")

class AuditReport(BaseModel):
    project_id: str
    run_hash: str = Field(..., description="Unique ID proving this exact run's provenance")
    results: list[SegmentResult]