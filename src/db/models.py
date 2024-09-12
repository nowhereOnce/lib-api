from sqlmodel import SQLModel, Field,Column, Relationship
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional, List

#Table Models

class Rocks(SQLModel, table=True):
    """
    This class represents a rock in the database
    """
    uid: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    description: str | None = None
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at:datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    
    # Relationship with Samples
    samples: List["Samples"] = Relationship(back_populates="rock")


class Locations(SQLModel, table=True):
    """
    This class represents a location in the database
    """
    uid: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    country: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at:datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    
    # Relationship with Samples
    samples: List["Samples"] = Relationship(back_populates="location")

class Samples(SQLModel, table=True):
    """
    This class represents a sample in the database (Has relationships with Rocks and Locations)
    """
    uid: UUID = Field(default_factory=uuid4, primary_key=True)
    rock_uid: UUID = Field(default=None, foreign_key="rocks.uid")
    location_uid: UUID = Field(default=None, foreign_key="locations.uid")
    cut: bool
    thin_section: bool
    picture: str #subject to change
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at:datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    
    # Relationship with Rocks
    rock: Optional[Rocks] = Relationship(back_populates="samples")
    
    # Relationship with Locations
    location: Optional[Locations] = Relationship(back_populates="samples")