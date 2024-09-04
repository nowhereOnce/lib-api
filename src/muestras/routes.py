from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from src.db.main import get_session
from http import HTTPStatus
from .service import MuestraService
from .schemas import MuestraCreateModel, MuestraResponseModel

muestras_router = APIRouter(prefix="/muestras")

#METODOS DE RUTAS PARA LAS MUESTRAS--------------------------------------------

@muestras_router.get("/", response_model=List[MuestraResponseModel]) 
async def read_muestras(session: AsyncSession = Depends(get_session)):
    """Obtiene todas las muestras"""
    muestras = await MuestraService(session).get_all_muestras()
    return muestras

#modificar para los casos donde no se encuentres el id o sea del tamaño incorrecto (37 caracteres)
@muestras_router.get("/{muestra_id}", status_code=HTTPStatus.OK)
async def read_muestra(muestra_id: str, session: AsyncSession = Depends(get_session)):
    """Obtiene una muestra por su UUID"""
    muestra = await MuestraService(session).get_roca(muestra_id)
    return muestra

@muestras_router.post("/", status_code=HTTPStatus.CREATED)
async def create_muestra(
    muestra_create_data: MuestraCreateModel, session: AsyncSession = Depends(get_session)
):
    """Crea una nueva muestra"""
    new_muestra = await MuestraService(session).create_muestra(muestra_create_data)

    return new_muestra

#modificar para los casos donde no se encuentres el id o sea del tamaño incorrecto (37 caracteres)
#decidir si se quiere conservar el atributo updated_at o no
#en caso de conservarlo es necesario que también se actualice la informacion del registro
@muestras_router.put("/{muestra_id}", status_code=HTTPStatus.OK)
async def update_muestra(
    muestra_id: str,
    update_data: MuestraCreateModel,
    session: AsyncSession = Depends(get_session),
):
    """Actualiza una muestra"""
    updated_muestra = await MuestraService(session).update_roca(muestra_id, update_data)

    return updated_muestra

@muestras_router.delete("/{muestra_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_muestra(muestra_id: str, session: AsyncSession = Depends(get_session)):
    """Borra una muestra"""
    await MuestraService(session).delete_muestra(muestra_id)
    return {}