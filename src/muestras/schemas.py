from src.db.models import Muestras, Rocas, Localidades
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

# NOTA: Probablemente sea necesario crear otro modelo de respuesta de las muestras donde se
# muestren las muestras filtradas por roca y localidad en lugar de su UID

#Verificar si es necesario que esta clase herede de la clase Rocas
class MuestraResponseModel(BaseModel):
    """
        Clase para validad la respuesta de muestra
    """
    uid: UUID
    roca_uid: UUID
    localidad_uid: UUID
    corte: bool
    lamina_delgada: bool
    foto: str #problablemente se tenga que modificar
    created_at: datetime
    updated_at: datetime

    model_config = {
        "json_schema_extra": {
            "example": {
                "uid": "a5b6c7d8e9f10",
                "roca_uid": "a5b6c7d8e9f10",
                "localidad_uid": "a5b6c7d8e9f10",
                "corte": True,
                "lamina_delgada": True,
                "fotos": "url_foto",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }
    }

class MuestraCreateModel(BaseModel):
    """
    Esta clase se usa para validar las solicitudes al crear o actualizar una muestra.
    """
    roca_uid: UUID
    localidad_uid: UUID
    corte: bool
    lamina_delgada: bool
    foto: str #problablemente se tenga que modificar

    model_config = {
        "json_schema_extra": {
            "example": {
                "roca_uid": "a5b6c7d8e9f10",
                "localidad_uid": "a5b6c7d8e9f10",
                "corte": True,
                "lamina_delgada": True,
                "foto": "url_foto",
            }
        }
    }
