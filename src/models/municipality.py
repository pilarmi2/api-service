from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/municipalities",
    tags=["Municipalities"],
)


class Municipality(BaseModel):
    """
    Represents a municipality.

    Attributes:
        municipality_id (int): The ID of the municipality.
        name (str): The name of the municipality.
        citizens (int, optional): The number of citizens in the municipality. Defaults to None.
    """

    municipality_id: int
    name: str
    citizens: int = None