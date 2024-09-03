from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.books.routes import rocas_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is starting")
    await init_db()
    yield
    print("server is shutting down")


app = FastAPI(
    title="muestras_rocas",
    version="0.1.0",
    description="API para la Plataforma del Instituto de Geología",
    lifespan=lifespan,
)


app.include_router(rocas_router, tags=["rocas"])
