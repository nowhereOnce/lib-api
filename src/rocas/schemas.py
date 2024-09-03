from src.db.models import Book, Rocas, Localidades, Muestras
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class BookResponseModel(Book):
    """
        This class is used to validate the response when getting book objects
    """
    pass

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

class LocalidadResponseModel(Book):
    """
        Clase para validad la respuesta de localidad
    """
    pass

class MuestraResponseModel(Book):
    """
        Clase para validad la respuesta de muestra
    """
    pass


class BookCreateModel(BaseModel):
    """
        This class is used to validate the request when creating or updating a book
    """
    title: str
    author: str
    isbn: str
    description: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Python Cookbook",
                "author": "John Doe",
                "isbn": "978-1-4939-1387-3",
                "description": "Python Cookbook is a collection of books written by <NAME> and <NAME>.",
            }
        }
    }

#ESQUEMAS PARA EL API DE ROCAS
#-------------------------------------------------------------------
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

class LocalidadCreateModel(BaseModel):
    """
    Esta clase se usa para validar las solicitudes al crear o actualizar una localidad.
    """
    nombre: str
    pais: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "nombre": "Liverpool",
                "pais": "Inglaterra.",
            }
        }
    }

class MuestraCreateModel(BaseModel):
    roca_uid: UUID
    localidad_uid: UUID
    corte: bool
    lamina_delgada: bool
    foto: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "roca_uid": "550e8400-e29b-41d4-a716-446655440000",
                "localidad_uid": "550e8400-e29b-41d4-a716-446655440001",
                "corte": True,
                "lamina_delgada": False,
                "foto": "url_con_foto_de_la_muestra"
            }
        }
    }