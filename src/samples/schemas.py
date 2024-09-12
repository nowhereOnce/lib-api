from src.db.models import Samples, Rocks, Locations
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class SampleResponseModel(BaseModel):
    """
        Class to validate the "sample" type response
    """
    uid: UUID
    cut: bool
    thin_section: bool
    picture: str
    created_at: datetime
    updated_at: datetime
    rock_name: str
    rock_description: str
    location_name: str
    location_country: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "uid": "a5b6c7d8e9f10",
                "cut": True,
                "thin_section": True,
                "picture": "url_foto",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
                "rock_name": "nombre_roca",
                "rock_description": "descripcion_roca",
                "location_name": "location_name",
                "location_country": "location_country"
            }
        }
    }

class SampleCreateModel(BaseModel):
    """
    Class to validate the requests to create/update a sample.
    """
    rock_uid: UUID
    location_uid: UUID
    cut: bool
    thin_section: bool
    picture: str # subject to change

    model_config = {
        "json_schema_extra": {
            "example": {
                "rock_uid": "a5b6c7d8e9f10",
                "location_uid": "a5b6c7d8e9f10",
                "cut": True,
                "thin_section": True,
                "picture": "url_picture",
            }
        }
    }
