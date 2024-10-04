from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from api import router as api_router
from core.config import settings
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup app
    yield
    # shutdown app
    await db_helper.dispose()


main_app = FastAPI(
    lifespan=lifespan,
)
main_app.include_router(api_router, prefix=settings.api_prefix.prefix)

if __name__ == "__main__":
    uvicorn.run("main:main_app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)
