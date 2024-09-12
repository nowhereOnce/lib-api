from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from src.db.main import get_session
from http import HTTPStatus
from .service import RockService
from .schemas import RockCreateModel, RockResponseModel

rocks_router = APIRouter(prefix="/rocks")

# ROCKS METHODS --------------------------------------------

@rocks_router.get("/", response_model=List[RockResponseModel]) 
async def read_rocks(session: AsyncSession = Depends(get_session)):
    """Gets all the rocks"""
    rocks = await RockService(session).get_all_rocks()
    return rocks

# modify for cases where the id is: not found / incorrect length (37 characters)
@rocks_router.get("/{rock_id}", status_code=HTTPStatus.OK)
async def read_rock(rock_id: str, session: AsyncSession = Depends(get_session)):
    """Gets a rock by its UUID"""
    rock = await RockService(session).get_rock(rock_id)
    return rock

@rocks_router.post("/", status_code=HTTPStatus.CREATED)
async def create_rock(
    rock_create_data: RockCreateModel, session: AsyncSession = Depends(get_session)
):
    """Creates a new rock"""
    new_rock = await RockService(session).create_rock(rock_create_data)

    return new_rock

# Modify for cases where the id is: not found / incorrect length (37 characters)
# Modify to update the update attribute 
@rocks_router.put("/{rock_id}", status_code=HTTPStatus.OK)
async def update_rock(
    rock_id: str,
    update_data: RockCreateModel,
    session: AsyncSession = Depends(get_session),
):
    """Updates a rock"""
    updated_rock = await RockService(session).update_rock(rock_id, update_data)

    return updated_rock

@rocks_router.delete("/{rock_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_rock(rock_id: str, session: AsyncSession = Depends(get_session)):
    """Deletes a rock"""
    await RockService(session).delete_rock(rock_id)
    return {}