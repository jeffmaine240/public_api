from pydantic import BaseModel
from datetime import datetime


class UserDetails(BaseModel):
    email : str
    current_datetime:datetime
    github_url: str