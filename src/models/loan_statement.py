from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities/{municipality_id}/loansStatements",
    tags=["Loans statements"]
)


class LoanStatement(BaseModel):
    """
    Represents a loan of a municipality.

    Attributes:
        municipality_id (int): The ID of the municipality.
        purpose (str): The purpose for which the loan was taken.
        agreed_amount (int): The agreed amount of the loan.
        drawn_amount (int): The amount of the loan that has been drawn down.
        repaid_amount (int): The amount of the loan that has been repaid.
        maturity_date (str): The maturity date of the loan.
        period (str): The period the statement of this loan is for.
    """

    municipality_id: str
    purpose: str
    agreed_amount: float
    drawn_amount: float
    repaid_amount: float
    maturity_date: str
    period: str
