from typing import Optional, List

from src.integrations.finance_monitor import FinanceMonitor
from src.integrations.store_service import StoreService
from src.models.loan_statement import router, LoanStatement
from src.models.standard_response import StandardResponse

finance_monitor: FinanceMonitor = FinanceMonitor()
store_service: StoreService = StoreService()


@router.get('')
async def search_loans_statement(
        municipality_id: str,
        period: str
) -> Optional[List[LoanStatement]]:
    loans_statements: list[LoanStatement] = finance_monitor.get_loans_statements(municipality_id, period)
    for loan_statement in loans_statements:
        response: StandardResponse = store_service.post_loan_statement(loan_statement)
        if response.status != 200:
            return None

    return loans_statements
