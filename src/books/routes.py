# Book API endpoints

from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from src.db.main import get_session
from http import HTTPStatus
from .service import RocaService
from .schemas import RocaCreateModel, RocaResponseModel

rocas_router = APIRouter(prefix="/rocas")

#METODOS DE RUTAS PARA ROCA--------------------------------------------

@rocas_router.get("/", response_model=List[RocaResponseModel]) 
async def read_rocas(session: AsyncSession = Depends(get_session)):
    """Obtiene todas las rocas"""
    rocas = await RocaService(session).get_all_rocas()
    return rocas

#modificar para los casos donde no se encuentres el id o sea del tamaño incorrecto (37 caracteres)
@rocas_router.get("/{roca_id}", status_code=HTTPStatus.OK)
async def read_roca(roca_id: str, session: AsyncSession = Depends(get_session)):
    """Gbtiene una roca por su UUID"""
    roca = await RocaService(session).get_roca(roca_id)
    return roca

@rocas_router.post("/", status_code=HTTPStatus.CREATED)
async def create_roca(
    roca_create_data: RocaCreateModel, session: AsyncSession = Depends(get_session)
):
    """Crea una nueva roca"""
    new_roca = await RocaService(session).create_roca(roca_create_data)

    return new_roca

#modificar para los casos donde no se encuentres el id o sea del tamaño incorrecto (37 caracteres)
#decidir si se quiere conservar el atributo updated_at o no
#en caso de conservarlo es necesario que también se actualice la informacion del registro
@rocas_router.put("/{roca_id}", status_code=HTTPStatus.OK)
async def update_roca(
    roca_id: str,
    update_data: RocaCreateModel,
    session: AsyncSession = Depends(get_session),
):
    """Actualiza una roca"""
    updated_roca = await RocaService(session).update_roca(roca_id, update_data)

    return updated_roca

@rocas_router.delete("/{roca_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_roca(roca_id: str, session: AsyncSession = Depends(get_session)):
    """Borra una roca"""
    await RocaService(session).delete_roca(roca_id)
    return {}