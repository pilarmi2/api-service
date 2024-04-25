import json
import os

import requests

from src.models.income_statement import IncomeStatement
from src.models.loans_statement import LoansStatement
from src.models.municipality import Municipality
from src.models.standard_response import StandardResponse


class StoreService:
    def __init__(self):
        self.__url = os.environ["STORE_SERVICE"]

    def post_municipality(self, municipality: Municipality) -> StandardResponse:
        response = requests.post(self.__url + "/municipalities", data=municipality.json())
        return StandardResponse(status=response.status_code, message=response.text)

    def post_income_statement(self, income_statement: IncomeStatement) -> StandardResponse:
        response = requests.post(self.__url + f"/{income_statement.municipality_id}/incomeStatement",
                                 data=income_statement.json())
        return StandardResponse(status=response.status_code, message=response.text)

    def post_loans_statement(self, loans_statement: LoansStatement) -> StandardResponse:
        response = requests.post(self.__url + f"/{loans_statement.municipality_id}/loansStatement",
                                 data=loans_statement.json())
        return StandardResponse(status=response.status_code, message=response.text)
