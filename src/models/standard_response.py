from pydantic import BaseModel


class StandardResponse(BaseModel):
    """
    Represents a standard response format for API responses.

    Attributes:
        status (int): The status code of the response.
        message (str): A message providing additional information about the response.
    """
    status: int
    message: str
