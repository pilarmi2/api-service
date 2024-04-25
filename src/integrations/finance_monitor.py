from src.models.municipality import Municipality


class FinanceMonitor:
    def __init__(self):
        pass

    def get_municipality(self, municipality_id) -> Municipality:
        return Municipality(municipality_id=municipality_id, name="Prague", citizens=1377136)

    def get_income_statement(self, municipality_id, period):
        pass

    def get_loans_statement(self, municipality_id, period):
        pass