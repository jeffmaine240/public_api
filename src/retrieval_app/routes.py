from fastapi import APIRouter, status
from .schemas import UserDetails
from datetime import datetime
from pytz import utc

retrieve_router = APIRouter()

@retrieve_router.get("/", response_model=UserDetails, status_code=status.HTTP_200_OK)
async def get_details() -> UserDetails:
    message = {
        "email" : "oyeniyij43@gmail.com",
        "current_datetime": datetime.now(utc).isoformat(),
        "github_url": "https://github.com/jeffmaine240/public_api"
    }
    
    return message