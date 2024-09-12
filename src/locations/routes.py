from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from src.db.main import get_session
from http import HTTPStatus
from .service import LocationService
from .schemas import LocationResponseModel, LocationCreateModel

locations_router = APIRouter(prefix="/locations")

# LOCATIONS METHODS --------------------------------------------

@locations_router.get("/", response_model=List[LocationResponseModel]) 
async def read_locations(session: AsyncSession = Depends(get_session)):
    """Gets all the locations"""
    locations = await LocationService(session).get_all_locations()
    return locations

# Modify for cases where the id is: not found / incorrect length (37 characters)
@locations_router.get("/{location_id}", status_code=HTTPStatus.OK)
async def read_location(location_id: str, session: AsyncSession = Depends(get_session)):
    """Gets a location by its UUID"""
    location = await LocationService(session).get_location(location_id)
    return location

@locations_router.post("/", status_code=HTTPStatus.CREATED)
async def create_location(
    location_create_data: LocationCreateModel, session: AsyncSession = Depends(get_session)
):
    """Creates a new location"""
    new_location = await LocationService(session).create_location(location_create_data)

    return new_location

# Modify for cases where the id is: not found / incorrect length (37 characters)
# Modify to update the update attribute 
@locations_router.put("/{location_id}", status_code=HTTPStatus.OK)
async def update_location(
    location_id: str,
    update_data: LocationCreateModel,
    session: AsyncSession = Depends(get_session),
):
    """Updates a location"""
    updated_location = await LocationService(session).update_location(location_id, update_data)

    return updated_location

@locations_router.delete("/{location_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_location(location_id: str, session: AsyncSession = Depends(get_session)):
    """Deletes a location"""
    await LocationService(session).delete_location(location_id)
    return {}