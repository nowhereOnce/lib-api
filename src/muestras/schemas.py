from src.db.models import Muestras, Rocas, Localidades
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class MuestraResponseModel(BaseModel):
    """
        Clase para validad la respuesta de muestra
    """
    uid: UUID
    corte: bool
    lamina_delgada: bool
    foto: str
    created_at: datetime
    updated_at: datetime
    nombre_roca: str
    descripcion_roca: str
    nombre_localidad: str
    pais_localidad: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "uid": "a5b6c7d8e9f10",
                "corte": True,
                "lamina_delgada": True,
                "foto": "url_foto",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
                "nombre_roca": "nombre_roca",
                "descripcion_roca": "descripcion_roca",
                "nombre_localidad": "nombre_localidad",
                "pais_localidad": "pais_localidad"
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
