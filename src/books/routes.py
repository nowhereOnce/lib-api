# Book API endpoints

from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from src.db.main import get_session
from http import HTTPStatus
from .service import BookService, RocaService
from .schemas import BookCreateModel, BookResponseModel, RocaCreateModel, RocaResponseModel

book_router = APIRouter(prefix="/books")


# @book_router.get("/", response_model=List[BookResponseModel])
# async def read_books(session: AsyncSession = Depends(get_session)):
#     """Get all books"""
#     books = await BookService(session).get_all_books()
#     return books


# @book_router.post("/", status_code=HTTPStatus.CREATED)
# async def create_book(
#     book_create_data: BookCreateModel, session: AsyncSession = Depends(get_session)
# ):
#     """Create a new book"""
#     new_book = await BookService(session).create_book(book_create_data)

#     return new_book


@book_router.get("/{book_id}", status_code=HTTPStatus.OK)
async def read_book(book_id: str, session: AsyncSession = Depends(get_session)):
    """Get a book by its uid"""
    book = await BookService(session).get_book(book_id)
    return book


@book_router.put("/{book_id}", status_code=HTTPStatus.OK)
async def update_book(
    book_id: str,
    update_data: BookCreateModel,
    session: AsyncSession = Depends(get_session),
):
    """Update a book"""
    updated_book = await BookService(session).update_book(book_id, update_data)

    return updated_book


@book_router.delete("/{book_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_book(book_id: str, session: AsyncSession = Depends(get_session)):
    """Delete a book"""
    await BookService(session).delete_book(book_id)
    return {}

#METODOS DE RUTAS PARA ROCA--------------------------------------------

@book_router.get("/", response_model=List[RocaResponseModel]) 
async def read_rocas(session: AsyncSession = Depends(get_session)):
    """Obtiene todas las rocas"""
    rocas = await RocaService(session).get_all_rocas()
    return rocas

@book_router.post("/", status_code=HTTPStatus.CREATED)
async def create_roca(
    roca_create_data: RocaCreateModel, session: AsyncSession = Depends(get_session)
):
    """Crea una nueva roca"""
    new_roca = await RocaService(session).create_roca(roca_create_data)

    return new_roca