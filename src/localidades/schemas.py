from src.db.models import Localidades
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

#Verificar si es necesario que esta clase herede de la clase Rocas
class LocalidadResponseModel(BaseModel):
    """
        Clase para validad la respuesta de roca
    """
    uid: UUID
    nombre: str
    pais: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "json_schema_extra": {
            "example": {
                "uid": "a0a0a0a0-a0a0-a0a0-a0a0-a0a0a0a0a0a0a",
                "nombre": "Cordoba",
                "pais": "Argentina",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }
    }

class LocalidadCreateModel(BaseModel):
    """
    Esta clase se usa para validar las solicitudes al crear o actualizar una roca.
    """
    nombre: str
    pais: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "nombre": "Cordoba",
                "pais": "Argentina",
            }
        }
    }
