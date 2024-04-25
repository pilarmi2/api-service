from src.models.income_statement import IncomeStatement
from src.models.loans_statement import LoansStatement
from src.models.municipality import Municipality


class FinanceMonitor:
    def __init__(self):
        pass

    def get_municipality(self, municipality_id) -> Municipality:
        return Municipality(municipality_id=municipality_id, name="Prague", citizens=1377136)

    def get_income_statement(self, municipality_id, period) -> IncomeStatement:
        return IncomeStatement(municipality_id=municipality_id, assets=1000, passives=500, period=period)

    def get_loans_statement(self, municipality_id, period) -> LoansStatement:
        return LoansStatement(municipality_id=municipality_id, purpose="Mortgage", agreed_amount=1000,
                              drawn_amount=1000, repaid_amount=500, maturity_date="2025-12-310", period=period)
