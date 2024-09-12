from src.db.models import Rocks
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class RockResponseModel(BaseModel):
    """
        Class to validate the "rock" type response
    """
    uid: UUID
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "json_schema_extra": {
            "example": {
                "uid": "a0a0a0a0-a0a0-a0a0-a0a0-a0a0a0a0a0a0a",
                "name": "Granito",
                "description": "Roca ígnea plutónica con textura granular.",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }
    }

class RockCreateModel(BaseModel):
    """
    Class to validate al the requests to create/update a rock
    """
    name: str
    description: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Granito",
                "description": "Roca ígnea plutónica con textura granular.",
            }
        }
    }
