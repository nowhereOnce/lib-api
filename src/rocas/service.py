from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import Rocks
from .schemas import RockCreateModel
from sqlmodel import select


class RockService:
    """
    This class provides all the methods to create, read, update and delete rocks from the Rocks table
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_rocks(self):
        """
        Gets a list with all the rocks

        Returns:
            list: list of rocks
        """
        statement = select(Rocks).order_by(Rocks.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def create_rock(self, rock_create_data: RockCreateModel):
        """
        Creates a new rock in the database

        Args:
            rock_create_data (RockCreateModel): data to create a new rock

        Returns:
            Rocks: a new rock
        """
        new_rock = Rocks(**rock_create_data.model_dump())
        self.session.add(new_rock)
        await self.session.commit()
        return new_rock

    async def get_rock(self, rock_uid: str):
        """Gets a rock by its UUID.

        Args:
            rock_uid (str): rock's UUID 

        Returns:
            Rocks: a rock object
        """
        statement = select(Rocks).where(Rocks.uid == rock_uid)
        result = await self.session.exec(statement)
        return result.first()

    async def update_rock(self, rock_uid: str, rock_update_data: RockCreateModel):
        """Updates a rock

        Args:
            rock_uid (str): rock's UUID
            rock_update_data (RockCreateModel): data to update the rock

        Returns:
            Rocks: updated rock
        """

        statement = select(Rocks).where(Rocks.uid == rock_uid)
        result = await self.session.exec(statement)
        rock = result.first()
        for key, value in rock_update_data.model_dump().items():
            setattr(rock, key, value)
        await self.session.commit()
        return rock

    async def delete_rock(self, rock_uid):
        """Deletes a rock

        Args:
            rock_uid (str): rock's UUID
        """
        statement = select(Rocks).where(Rocks.uid == rock_uid)
        result = await self.session.exec(statement)
        rock = result.first()
        await self.session.delete(rock)
        await self.session.commit()
