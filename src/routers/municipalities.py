from typing import Optional

from src.models.municipality import router, Municipality


@router.get("/{municipality_id}")
async def search_municipality_by_id(
        municipality_id: int
) -> Optional[Municipality]:
    return Municipality(municipality_id=municipality_id, name="Prague", citizens=1377136)
