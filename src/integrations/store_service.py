import json
import os
import requests

from src.models.income_statement import IncomeStatement
from src.models.loan_statement import LoanStatement
from src.models.municipality import Municipality
from src.models.standard_response import StandardResponse


class StoreService:
    def __init__(self):
        """
        Initialize StoreService class.
        """
        self.__url = os.environ["STORE_SERVICE"]

    def post_municipality(self, municipality: Municipality) -> StandardResponse:
        """
        Post municipality data to the store service.

        Args:
            municipality (Municipality): The Municipality object to post.

        Returns:
            StandardResponse: The response from the store service.
        """
        response = requests.post(self.__url + "/municipalities", data=municipality.json())
        print(response.text)
        return StandardResponse(status=response.status_code, message=response.text)

    def post_income_statement(self, income_statement: IncomeStatement) -> StandardResponse:
        """
        Post income statement data to the store service.

        Args:
            income_statement (IncomeStatement): The IncomeStatement object to post.

        Returns:
            StandardResponse: The response from the store service.
        """
        response = requests.post(self.__url + f"/municipalities/{income_statement.municipality_id}/incomeStatement",
                                 data=income_statement.json())
        print(response.text)
        return StandardResponse(status=response.status_code, message=response.text)

    def post_loan_statement(self, loan_statement: LoanStatement) -> StandardResponse:
        """
        Post loan statement data to the store service.

        Args:
            loan_statement (LoanStatement): The LoanStatement object to post.

        Returns:
            StandardResponse: The response from the store service.
        """
        response = requests.post(self.__url + f"/municipalities/{loan_statement.municipality_id}/loansStatements",
                                 data=loan_statement.json())

        print(response.text)
        return StandardResponse(status=response.status_code, message=response.text)
