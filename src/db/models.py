from sqlmodel import SQLModel, Field,Column, Relationship
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional, List

class Book(SQLModel, table = True):
    """
    This class represents a book in the database
    """
    __tablename__ = 'books'
    uid:UUID = Field(
        sa_column=Column(pg.UUID ,primary_key=True,
        unique=True, default=uuid4)
    )
    title:str
    author:str
    isbn:str
    description:str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at:datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self) -> str:
        return f"Book => {self.title}"

# Clases de la base de datos de rocas
#------------------------------------------------------------------
class Rocas(SQLModel, table=True):
    """
    Esta clase representa una roca en la base de datos
    """
    uid: UUID = Field(default_factory=uuid4, primary_key=True)
    nombre: str
    descripcion: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at:datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    
    # Relación con Muestras
    muestras: List["Muestras"] = Relationship(back_populates="roca")


class Localidades(SQLModel, table=True):
    """
    Esta clase representa una localidad en la base de datos
    """
    uid: UUID = Field(default_factory=uuid4, primary_key=True)
    nombre: str
    pais: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at:datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    
    # Relación con Muestras
    muestras: List["Muestras"] = Relationship(back_populates="localidad")

class Muestras(SQLModel, table=True):
    """
    Esta clase representa una muestra con roca y localidad en la base de datos
    """
    uid: UUID = Field(default_factory=uuid4, primary_key=True)
    roca_uid: UUID = Field(default=None, foreign_key="rocas.uid")
    localidad_uid: UUID = Field(default=None, foreign_key="localidades.uid")
    corte: bool
    lamina_delgada: bool
    foto: str #probablemente se tenga que modificar
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at:datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    
    # Relación con Rocas
    roca: Optional[Rocas] = Relationship(back_populates="muestras")
    
    # Relación con Localidades
    localidad: Optional[Localidades] = Relationship(back_populates="muestras")