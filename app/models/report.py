from pydantic import BaseModel

class ReportInput(BaseModel):
    cxr_report: str
    ct_report: str