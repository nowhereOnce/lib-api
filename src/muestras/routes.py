from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from src.db.main import get_session
from http import HTTPStatus
from .service import SampleService
from .schemas import SampleCreateModel, SampleResponseModel

samples_router = APIRouter(prefix="/samples")

# SAMPLES METHODS --------------------------------------------

@samples_router.get("/", response_model=List[SampleResponseModel]) 
async def read_samples(session: AsyncSession = Depends(get_session)):
    """Gets all the samples"""
    samples = await SampleService(session).get_all_samples()
    return samples

# Modify for cases where the id is: not found / incorrect length (37 characters)
@samples_router.get("/{sample_id}", status_code=HTTPStatus.OK)
async def read_sample(sample_id: str, session: AsyncSession = Depends(get_session)):
    """Gets a sample by its UUID"""
    sample = await SampleService(session).get_sample(sample_id)
    return sample

@samples_router.post("/", status_code=HTTPStatus.CREATED)
async def create_sample(
    sample_create_data: SampleCreateModel, session: AsyncSession = Depends(get_session)
):
    """Creates a new sample"""
    new_sample = await SampleService(session).create_sample(sample_create_data)

    return new_sample

# Modify for cases where the id is: not found / incorrect length (37 characters)
# Modify to update the update attribute 
@samples_router.put("/{sample_id}", status_code=HTTPStatus.OK)
async def update_sample(
    sample_id: str,
    update_data: SampleCreateModel,
    session: AsyncSession = Depends(get_session),
):
    """Updates a sample"""
    updated_sample = await SampleService(session).update_sample(sample_id, update_data)

    return updated_sample

@samples_router.delete("/{sample_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_sample(sample_id: str, session: AsyncSession = Depends(get_session)):
    """Deletes a sample"""
    await SampleService(session).delete_sample(sample_id)
    return {}