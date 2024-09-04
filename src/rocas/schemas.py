from src.db.models import Rocas
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

#Verificar si es necesario que esta clase herede de la clase Rocas
class RocaResponseModel(BaseModel):
    """
        Clase para validad la respuesta de roca
    """
    uid: UUID
    nombre: str
    descripcion: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "json_schema_extra": {
            "example": {
                "uid": "a0a0a0a0-a0a0-a0a0-a0a0-a0a0a0a0a0a0a",
                "nombre": "Granito",
                "descripcion": "Roca ígnea plutónica con textura granular.",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }
    }

class RocaCreateModel(BaseModel):
    """
    Esta clase se usa para validar las solicitudes al crear o actualizar una roca.
    """
    nombre: str
    descripcion: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "nombre": "Granito",
                "descripcion": "Roca ígnea plutónica con textura granular.",
            }
        }
    }
