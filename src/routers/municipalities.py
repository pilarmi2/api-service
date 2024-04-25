from typing import Optional

from src.integrations.ares_portal import AresPortal
from src.integrations.finance_monitor import FinanceMonitor
from src.integrations.store_service import StoreService
from src.models.municipality import router, Municipality
from src.models.standard_response import StandardResponse

finance_monitor: FinanceMonitor = FinanceMonitor()
store_service: StoreService = StoreService()
ares_portal: AresPortal = AresPortal()


@router.get("/{municipality_id}")
async def search_municipality_by_id(
        municipality_id: str
) -> Optional[Municipality]:
    municipality = finance_monitor.get_municipality(municipality_id)
    municipality.name = ares_portal.get_municipality_name(municipality_id)
    response: StandardResponse = store_service.post_municipality(municipality)

    if response.status == 200:
        return municipality
    else:
        return None
