from typing import Optional

from src.integrations.finance_monitor import FinanceMonitor
from src.integrations.store_service import StoreService
from src.models.municipality import router, Municipality
from src.models.standard_response import StandardResponse

finance_monitor: FinanceMonitor = FinanceMonitor()
store_service: StoreService = StoreService()


@router.get("/{municipality_id}")
async def search_municipality_by_id(
        municipality_id: int
) -> Optional[Municipality]:
    municipality = finance_monitor.get_municipality(municipality_id)
    response: StandardResponse = store_service.post_municipality(municipality)

    if response.status == 200:
        return municipality
    else:
        return None
