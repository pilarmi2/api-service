from src.models.municipality import Municipality
from src.models.standard_response import StandardResponse


class StoreService:
    def __init__(self):
        pass

    def post_municipality(self, municipality: Municipality) -> StandardResponse:
        return StandardResponse(status=200, message="POSTED")

    def post_income_statement(self, income_statement) -> StandardResponse:
        return StandardResponse(status=200, message="POSTED")

    def post_loans_statement(self, loans_statement) -> StandardResponse:
        return StandardResponse(status=200, message="POSTED")