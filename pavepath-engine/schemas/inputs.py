from pydantic import BaseModel, Field

class SurveyPoint(BaseModel):
    point_id: str = Field(..., description="Unique ID or number for the survey point")
    easting: float = Field(..., description="X coordinate")
    northing: float = Field(..., description="Y coordinate")
    elevation: float = Field(..., description="Z coordinate")
    description: str = Field(..., description="Civil 3D Feature line tag, e.g., SW-EDGE")

class Civil3DExport(BaseModel):
    project_id: str = Field(..., description="Internal PavePath project number")
    rule_pack_version: str = Field(..., description="Which ADA/PROWAG rule pack applies")
    points: list[SurveyPoint]