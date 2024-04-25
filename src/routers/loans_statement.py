from typing import Optional

from src.integrations.finance_monitor import FinanceMonitor
from src.integrations.store_service import StoreService
from src.models.loans_statement import router, LoansStatement
from src.models.standard_response import StandardResponse

finance_monitor: FinanceMonitor = FinanceMonitor()
store_service: StoreService = StoreService()


@router.get('')
async def search_loans_statement(
        municipality_id: int,
        period: str
) -> Optional[LoansStatement]:
    loans_statement = finance_monitor.get_loans_statement(municipality_id, period)
    response: StandardResponse = store_service.post_loans_statement(loans_statement)

    if response.status == 200:
        return loans_statement
    else:
        return None
