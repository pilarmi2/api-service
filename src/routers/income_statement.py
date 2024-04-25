from src.models.income_statement import router


@router.get('')
async def search_income_statement(
        municipality_id: int,
        period: str
):
    return {}
