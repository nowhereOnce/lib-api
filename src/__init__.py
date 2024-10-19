from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.rocks.routes import rocks_router
from src.locations.routes import locations_router
from src.samples.routes import samples_router
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is starting")
    await init_db()
    yield
    print("server is shutting down")


app = FastAPI(
    title="rocks_samples",
    version="0.1.0",
    description="Insituto de Geología rocks_samples API",
    lifespan=lifespan,
)

# Configuración del middleware CORS (Para conectar con el front)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  #Direccion donde se está ejecutando en front-end
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rocks_router, tags=["rocks"])
app.include_router(locations_router, tags=["locations"])
app.include_router(samples_router, tags=["samples"])
