from src.db.models import Locations
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class LocationResponseModel(BaseModel):
    """
        Class to validate the "location" type response
    """
    uid: UUID
    name: str
    country: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "json_schema_extra": {
            "example": {
                "uid": "a0a0a0a0-a0a0-a0a0-a0a0-a0a0a0a0a0a0a",
                "name": "Cordoba",
                "country": "Argentina",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }
    }

class LocationCreateModel(BaseModel):
    """
    Class used to validate the requests to create/update a location.
    """
    name: str
    country: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Cordoba",
                "country": "Argentina",
            }
        }
    }
