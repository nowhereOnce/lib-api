from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.rocas.routes import rocas_router
from src.localidades.routes import localidades_router
from src.muestras.routes import muestras_router


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
app.include_router(localidades_router, tags=["localidades"])
app.include_router(muestras_router, tags=["muestras"])
