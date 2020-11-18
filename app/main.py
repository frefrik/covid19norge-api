from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .routers import v1
from .utils import create_json_files
from .tasks import check_for_updates, get_datafiles
from .config import UPDATE_INTERVAL

scheduler = AsyncIOScheduler()
scheduler.start()

APP = FastAPI(
    title="COVID-19 Norway API",
    description=(
        "API for tracking the COVID-19 outbreak in Norway."
    ),
    version="0.1.0",
    docs_url="/api",
    redoc_url="/api/docs",
    on_startup=[get_datafiles, create_json_files],
    openapi_url="/api/openapi.json"
)

APP.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

scheduler.add_job(
    check_for_updates,
    'interval',
    seconds=UPDATE_INTERVAL
)

APP.include_router(v1, prefix="/api/v1", tags=["v1"])
