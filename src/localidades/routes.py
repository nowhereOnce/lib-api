from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from src.db.main import get_session
from http import HTTPStatus
from .service import LocalidadService
from .schemas import LocalidadResponseModel, LocalidadCreateModel

localidades_router = APIRouter(prefix="/localidades")

#METODOS DE RUTAS PARA LOCALIDADES--------------------------------------------

@localidades_router.get("/", response_model=List[LocalidadResponseModel]) 
async def read_localidades(session: AsyncSession = Depends(get_session)):
    """Obtiene todas las localidades"""
    localidades = await LocalidadService(session).get_all_localidades()
    return localidades

#modificar para los casos donde no se encuentres el id o sea del tamaño incorrecto (37 caracteres)
@localidades_router.get("/{localidad_id}", status_code=HTTPStatus.OK)
async def read_localidad(localidad_id: str, session: AsyncSession = Depends(get_session)):
    """Obtiene una localidad por su UUID"""
    localidad = await LocalidadService(session).get_localidad(localidad_id)
    return localidad

@localidades_router.post("/", status_code=HTTPStatus.CREATED)
async def create_localidad(
    localidad_create_data: LocalidadCreateModel, session: AsyncSession = Depends(get_session)
):
    """Crea una nueva localidad"""
    new_localidad = await LocalidadService(session).create_localidad(localidad_create_data)

    return new_localidad

#modificar para los casos donde no se encuentres el id o sea del tamaño incorrecto (37 caracteres)
#decidir si se quiere conservar el atributo updated_at o no
#en caso de conservarlo es necesario que también se actualice la informacion del registro
@localidades_router.put("/{localidad_id}", status_code=HTTPStatus.OK)
async def update_localidad(
    localidad_id: str,
    update_data: LocalidadCreateModel,
    session: AsyncSession = Depends(get_session),
):
    """Actualiza una localidad"""
    updated_localidad = await LocalidadService(session).update_localidad(localidad_id, update_data)

    return updated_localidad

@localidades_router.delete("/{localidad_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_localidad(localidad_id: str, session: AsyncSession = Depends(get_session)):
    """Borra una localidad"""
    await LocalidadService(session).delete_localidad(localidad_id)
    return {}