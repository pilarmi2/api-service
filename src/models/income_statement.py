from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities/{municipality_id}/incomeStatement",
    tags=["Income statements"]
)


class IncomeStatement(BaseModel):
    """
    Represents an income statement for a municipality.

    Attributes:
        municipality_id (int): The ID of the municipality.
        assets (int): The assets of the municipality.
        passives (int): The passives of the municipality.
        period (str): The period the income statement is for.
    """

    municipality_id: str
    assets: float
    passives: float
    period: str
