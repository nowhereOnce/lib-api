from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import text, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import settings

# async_engine: Es el motor de base de datos asíncrono que permite realizar operaciones en PostgreSQL.
async_engine = create_async_engine(url=settings.POSTGRES_URL, echo=True)

# init_db: Es una función que se encarga de crear las tablas en la base de datos utilizando la definición de los modelos.
async def init_db():
    """Create the database tables"""
    async with async_engine.begin() as conn:
        from .models import Book

        await conn.run_sync(SQLModel.metadata.create_all)

# get_session: Es una función que proporciona sesiones de base de datos asíncronas que pueden ser usadas para ejecutar operaciones en la base de datos.
async def get_session() -> AsyncSession:
    """Dependency to provide the session object"""
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session
