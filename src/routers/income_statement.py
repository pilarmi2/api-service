from typing import Optional

from src.integrations.finance_monitor import FinanceMonitor
from src.integrations.store_service import StoreService
from src.models.income_statement import router, IncomeStatement
from src.models.standard_response import StandardResponse

finance_monitor: FinanceMonitor = FinanceMonitor()
store_service: StoreService = StoreService()


@router.get('')
async def search_income_statement(
        municipality_id: str,
        period: str
) -> Optional[IncomeStatement]:
    income_statement = finance_monitor.get_income_statement(municipality_id, period)
    response: StandardResponse = store_service.post_income_statement(income_statement)

    if response.status == 200:
        return income_statement
    else:
        return None
