from src.models.loans_statement import router


@router.get('')
async def search_loans_statement(
        municipality_id: int,
        period: str
):
    return {}
