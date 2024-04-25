from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities/{municipality_id}/loansStatement",
    tags=["Loans statements"]
)


class LoansStatement(BaseModel):
    """
    Represents a statement of loans for a municipality.

    Attributes:
        municipality_id (int): The ID of the municipality.
        purpose (str): The purpose for which the loan was taken.
        agreed_amount (int): The agreed amount of the loan.
        drawn_amount (int): The amount of the loan that has been drawn down.
        repaid_amount (int): The amount of the loan that has been repaid.
        maturity_date (str): The maturity date of the loan.
        period (str): The period the statement of loans is for.
    """

    municipality_id: int
    purpose: str
    agreed_amount: int
    drawn_amount: int
    repaid_amount: int
    maturity_date: str
    period: str
