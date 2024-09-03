from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import Book, Rocas
from .schemas import BookCreateModel, RocaCreateModel
from sqlmodel import select


class RocaService:
    """
    Esta clase provee los metodos para crear, leer, actualizar, y eliminar rocas
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_rocas(self):
        """
        Obtiene una lista con todas las rocas

        Returns:
            list: una lista de rocas
        """
        statement = select(Rocas).order_by(Rocas.created_at)

        result = await self.session.exec(statement)

        return result.all()

    async def create_roca(self, roca_create_data: RocaCreateModel):
        """
        Crea una nueva roca en la base de datos

        Args:
            roca_create_data (RocaCreateModel): data para crear una nueva roca

        Returns:
            Rocas: una nueva roca
        """
        new_roca = Rocas(**roca_create_data.model_dump())

        self.session.add(new_roca)

        await self.session.commit()

        return new_roca

    async def get_roca(self, roca_uid: str):
        """Obtiene una roca por su UUID.

        Args:
            roca_uid (str): el UUID de la roca

        Returns:
            Rocas: un objeto roca
        """
        statement = select(Rocas).where(Rocas.uid == roca_uid)

        result = await self.session.exec(statement)

        return result.first()

    async def update_roca(self, roca_uid: str, roca_update_data: RocaCreateModel):
        """Actualiza una roca

        Args:
            roca_uid (str): el UUID de la roca
            roca_update_data (BookCreateModel): la data para actualizar la roca

        Returns:
            Rocas: la roca actualizada
        """

        statement = select(Rocas).where(Rocas.uid == roca_uid)

        result = await self.session.exec(statement)

        roca = result.first()

        for key, value in roca_update_data.model_dump().items():
            setattr(roca, key, value)

        await self.session.commit()

        return roca

    async def delete_roca(self, roca_uid):
        """Borra una roca

        Args:
            roca_uid (str): el UUID de la roca
        """
        statement = select(Rocas).where(Rocas.uid == roca_uid)
        result = await self.session.exec(statement)

        roca = result.first()

        await self.session.delete(roca)

        await self.session.commit()


class BookService:
    """
    class for books
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_books(self):
        """
        Get a list of all books

        Returns:
            list: list of books
        """
        statement = select(Book).order_by(Book.created_at)

        result = await self.session.exec(statement)

        return result.all()

    async def create_book(self, book_create_data: BookCreateModel):
        """
        Create a new book

        Args:
            book_create_data (BookCreateModel): data to create a new

        Returns:
            Book: the new book
        """
        new_book = Book(**book_create_data.model_dump())

        self.session.add(new_book)

        await self.session.commit()

        return new_book

    async def get_book(self, book_uid: str):
        """Get a book by its UUID.

        Args:
            book_uid (str): the UUID of the book

        Returns:
            Book: the book object
        """
        statement = select(Book).where(Book.uid == book_uid)

        result = await self.session.exec(statement)

        return result.first()

    async def update_book(self, book_uid: str, book_update_data: BookCreateModel):
        """Update a book

        Args:
            book_uid (str): the UUID of the book
            book_update_data (BookCreateModel): the data to update the book

        Returns:
            Book: the updated book
        """

        statement = select(Book).where(Book.uid == book_uid)

        result = await self.session.exec(statement)

        book = result.first()

        for key, value in book_update_data.model_dump().items():
            setattr(book, key, value)

        await self.session.commit()

        return book

    async def delete_book(self, book_uid):
        """Delete a book

        Args:
            book_uid (str): the UUID of the book
        """
        statement = select(Book).where(Book.uid == book_uid)
        result = await self.session.exec(statement)

        book = result.first()

        await self.session.delete(book)

        await self.session.commit()