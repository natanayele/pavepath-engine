from pydantic import BaseModel, Field

class SlopeRule(BaseModel):
    rule_id: str
    max_pass: float = Field(..., description="Maximum slope % to PASS (e.g., 5.0)")
    max_warn: float = Field(..., description="Maximum slope % to WARN (e.g., 8.33)")
    # Note: Any calculated slope strictly greater than max_warn triggers a FAIL.

class RulePack(BaseModel):
    pack_name: str = Field(..., description="e.g., PROWAG_FEDERAL, CALTRANS_ADA")
    version: str
    running_slope: SlopeRule
    cross_slope: SlopeRule