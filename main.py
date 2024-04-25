import os

from fastapi import FastAPI
from starlette.responses import RedirectResponse
import uvicorn

from src.routers import municipalities, income_statement, loans_statement

# load environment variables
port = int(os.environ["PORT"])
host = os.environ["HOST"]

app = FastAPI()
app.include_router(municipalities.router)
app.include_router(income_statement.router)
app.include_router(loans_statement.router)


@app.get("/", include_in_schema=False, response_class=RedirectResponse)
async def api_spec():
    return "/docs"


if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)