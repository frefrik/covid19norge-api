from fastapi import APIRouter
from fastapi.responses import FileResponse, JSONResponse
from ..config import (
    CURRENT_JSON_PATH,
    TIMESERIES_JSON_PATH,
    TIMESERIES_CONFIRMED_JSON_PATH,
    TIMESERIES_DEAD_JSON_PATH,
    TIMESERIES_TESTED_JSON_PATH,
    TIMESERIES_TESTED_LAB_JSON_PATH,
    TIMESERIES_HOSPITALIZED_JSON_PATH,
    TRANSPORT_JSON_PATH,
    TIMESERIES_VACCINE_DOSES_JSON_PATH,
)
from ..config import (
    TIMESERIES_EXAMPLE,
    TIMESERIES_CATEGORY_EXAMPLE,
    CURRENT_EXAMPLE,
    TRANSPORT_EXAMPLE,
)

v1 = APIRouter()


@v1.get(
    "/current",
    responses={200: {"content": {"application/json": {"example": CURRENT_EXAMPLE}}}},
)
async def current():
    """
    Get current key figures
    - **tested**: Tested cases
    - **confirmed**: Confirmed cases
    - **dead**: Dead cases
    - **admissions**: Admissions cases
    - **respiratory**: Respiratory cases
    - **vaccine_doses**: Vaccine doses administered
    """
    return FileResponse(CURRENT_JSON_PATH)


@v1.get(
    "/timeseries",
    responses={200: {"content": {"application/json": {"example": TIMESERIES_EXAMPLE}}}},
)
async def timeseries():
    """
    Timeseries data
    """
    return FileResponse(TIMESERIES_JSON_PATH)


@v1.get(
    "/timeseries/{category}",
    responses={
        200: {
            "content": {"application/json": {"example": TIMESERIES_CATEGORY_EXAMPLE}}
        },
        404: {
            "content": {"application/json": {"example": {"message": "Item not found"}}}
        },
    },
)
async def timeseries_category(category: str):
    """
    Available categories:
    - **tested**
    - **tested_lab**
    - **confirmed**
    - **dead**
    - **hospitalized**
    - **vaccine_doses**
    """
    categories = {
        "tested": TIMESERIES_TESTED_JSON_PATH,
        "tested_lab": TIMESERIES_TESTED_LAB_JSON_PATH,
        "confirmed": TIMESERIES_CONFIRMED_JSON_PATH,
        "dead": TIMESERIES_DEAD_JSON_PATH,
        "hospitalized": TIMESERIES_HOSPITALIZED_JSON_PATH,
        "vaccine_doses": TIMESERIES_VACCINE_DOSES_JSON_PATH,
    }

    if category not in categories:
        return JSONResponse(status_code=404, content={"message": "Item not found"})

    return FileResponse(categories[category])


@v1.get(
    "/transport",
    responses={200: {"content": {"application/json": {"example": TRANSPORT_EXAMPLE}}}},
)
async def transport():
    """
    List of departures where persons infected with covid-19 have been on board aircraft, ships, trains and buses.
    """
    return FileResponse(TRANSPORT_JSON_PATH)
