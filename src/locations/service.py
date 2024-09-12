from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import Locations
from .schemas import LocationCreateModel
from sqlmodel import select


class LocationService:
    """
    This class provides the methods to create, read, update and delete a location
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_locations(self):
        """
        Gets a list with all the locations

        Returns:
            list: list of locations
        """
        statement = select(Locations).order_by(Locations.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def create_location(self, location_create_data: LocationCreateModel):
        """
        Creates a new location in the database

        Args:
            location_create_data (LocationCreateModel): data to create a new location

        Returns:
            Location: a new location
        """
        new_location = Locations(**location_create_data.model_dump())
        self.session.add(new_location)
        await self.session.commit()
        return new_location

    async def get_location(self, location_uid: str):
        """Gets a location by its UUID.

        Args:
            location_uid (str): location's UUID

        Returns:
            Locations: an location object
        """
        statement = select(Locations).where(Locations.uid == location_uid)
        result = await self.session.exec(statement)
        return result.first()

    async def update_location(self, location_uid: str, location_update_data: LocationCreateModel):
        """Updates a location

        Args:
            location_uid (str): location's UIID
            location_update_data (LocationCreateModel): data to update the location

        Returns:
            Locations: updated location
        """

        statement = select(Locations).where(Locations.uid == location_uid)
        result = await self.session.exec(statement)
        location = result.first()
        for key, value in location_update_data.model_dump().items():
            setattr(location, key, value)
        await self.session.commit()
        return location

    async def delete_location(self, location_uid):
        """Deletes a location

        Args:
            location_uid (str): location's UIID
        """
        statement = select(Locations).where(Locations.uid == location_uid)
        result = await self.session.exec(statement)
        location = result.first()
        await self.session.delete(location)
        await self.session.commit()
