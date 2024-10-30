from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import Samples, Rocks, Locations
from .schemas import SampleCreateModel, SampleResponseModel
from sqlmodel import select


class SampleService:
    """
    This class provides theh methods to create, read, update and delete a sample
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_or_create_rock(self, rock_name: str, description: str):
        """
        Retrieves a rock from the database or creates it if it doesn't exist.

        Args:
            rock_name (str): The name of the rock.
            description (str): The description of the rock.

        Returns:
            Rocks: The existing or newly created rock object.
        """
        rock_statement = select(Rocks).where(Rocks.name == rock_name)
        rock_result = await self.session.exec(rock_statement)
        rock = rock_result.first()

        if not rock:
            rock = Rocks(name=rock_name, description=description)
            self.session.add(rock)
            await self.session.commit()
            await self.session.refresh(rock)
            print(f"\n[DEBUGGING] INSERTED ROCK's UID : {rock.uid}")

        print(f"\n[DEBUGGING] FOUND ROCK's UID: {rock.uid}")
        return rock

    async def get_or_create_location(self, location_name: str, country: str):
        """
        Retrieves a location from the database or creates it if it doesn't exist.

        Args:
            location_name (str): The name of the location.
            country (str): The country of the location.

        Returns:
            Locations: The existing or newly created location object.
        """
        location_statement = select(Locations).where(Locations.name == location_name)
        location_result = await self.session.exec(location_statement)
        location = location_result.first()

        if not location:
            location = Locations(name=location_name, country=country)
            self.session.add(location)
            await self.session.commit()
            await self.session.refresh(location)
            print(f"\n[DEBUGGING] INSERTED LOCATION's UID: {location.uid}")

        print(f"\n[DEBUGGING] FOUND LOCATION's UID: {location.uid}")
        return location

    async def create_sample(self, sample_create_data: SampleCreateModel):
        """
        Creates a new sample in the database.

        Args:
            sample_create_data (SampleCreateModel): The data to create a new sample.

        Returns:
            Samples: The newly created sample object.
        """
        rock = await self.get_or_create_rock(
            sample_create_data.rock_name, sample_create_data.description
        )
        location = await self.get_or_create_location(
            sample_create_data.location_name, sample_create_data.location_country
        )

        new_sample = Samples(
            rock_uid=rock.uid,
            location_uid=location.uid,
            cut=sample_create_data.cut,
            thin_section=sample_create_data.thin_section,
            picture=sample_create_data.picture
        )
        
        self.session.add(new_sample)
        await self.session.commit()
        await self.session.refresh(new_sample)
        
        return new_sample

    async def update_sample(self, sample_uid: str, sample_update_data: SampleCreateModel):
        """Updates a sample

        Args:
            sample_uid (str): sample's UUID
            sample_update_data (SampleCreateModel): data to update the sample

        Returns:
            Samples: updated sample
        """

        statement = select(Samples).where(Samples.uid == sample_uid)
        result = await self.session.exec(statement)
        sample = result.first()
        for key, value in sample_update_data.model_dump().items():
            setattr(sample, key, value)
        await self.session.commit()
        return sample

    async def delete_sample(self, sample_uid):
        """Deletes a sample

        Args:
            sample_uid (str): sample's UUID
        """
        statement = select(Samples).where(Samples.uid == sample_uid)
        result = await self.session.exec(statement)
        sample = result.first()
        await self.session.delete(sample)
        await self.session.commit()
