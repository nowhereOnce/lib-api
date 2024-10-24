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


    async def get_all_samples(self):
        """
        Gets a list with all the samples

        Returns:
            list: list of samples
        """
        statement = select(Samples, Rocks, Locations).join(Samples.rock).join(Samples.location).order_by(Samples.created_at)
        result = await self.session.exec(statement)
        return [SampleResponseModel(
            uid = sample.uid, 
            cut = sample.cut,
            thin_section = sample.thin_section,
            picture = sample.picture,
            created_at = sample.created_at,
            updated_at = sample.updated_at,
            rock_name = sample.rock.name,
            rock_description = sample.rock.description,
            location_name = sample.location.name,
            location_country = sample.location.country
            ) for sample, _, _ in result]

    # MODIFIED: to first check if the corresponding rock and location already exist in the BD:
    # if not: creates the rock and/or creates the location 
    # if it/they exist: uses the rock and location to create the new sample
    async def create_sample(self, sample_create_data: SampleCreateModel):
        """
        Creates a new sample in the database

        Args:
            sample_create_data (SampleCreateModel): data to create a new sample

        Returns:
            Samples: a new sample
        """
        #Looks for a rock in the DB
        rock_statement = select(Rocks).where(Rocks.name == sample_create_data.rock_name)
        rock_result = await self.session.exec(rock_statement)
        rock = rock_result.first() #Rocks object
        
        #If it wasnt in the db then it is created
        if not rock:
            rock = Rocks(name=sample_create_data.rock_name, description=sample_create_data.description)
            self.session.add(rock)
            await self.session.commit()
            await self.session.refresh(rock)
            print("\n[DEBUGGING] INSERTED ROCK's UID : " + str(rock.model_dump()["uid"])) #DEBUGGING
            print("[DEBUGGING] THE INSERTION WAS MADE SUCCESSFULLY \n") #DEBUGGING
        
        print("\n[DEBUGGING] FOUND ROCK's UID: " + str(rock.model_dump()["uid"])) #DEBUGGING
        
        # #Looks for a location in the DB (this line most likely will not work idk :c)
        location_statement = select(Locations).where(Locations.name == sample_create_data.location_name)
        location_result = await self.session.exec(location_statement)
        location = location_result.first() #Locations object
        
        # #If it wasnt in the db then it is created
        if not location:
            location = Locations(name=sample_create_data.location_name, country=sample_create_data.location_country)
            self.session.add(location)
            await self.session.commit()
            await self.session.refresh(location)
            print("\n[DEBUGGING] ISERTED LOCATION's UID: " + str(location.model_dump()["uid"])) #DEBUGGING
            print("[DEBUGGING] THE INSERTION WAS MADE SUCCESSFULLY \n") #DEBUGGING
        
        print("\n[DEBUGGING] FOUND LOCATION's UID: " + str(location.model_dump()["uid"])) #DEBUGGING
        
        # #Creates the new sample into the DB.
        new_sample = Samples(
            rock_uid = rock.model_dump()["uid"],
            location_uid=location.model_dump()["uid"],
            cut=sample_create_data.cut,
            thin_section= sample_create_data.thin_section,
            picture=sample_create_data.picture
            )
        
        self.session.add(new_sample)
        await self.session.commit()
        await self.session.refresh(new_sample)
        return new_sample


    async def get_sample(self, sample_uid: str):
        """Gets a sample by its UUID.

        Args:
            sample_uid (str): sample's UUID

        Returns:
            Samples: sample object
        """
        statement = select(Samples).where(Samples.uid == sample_uid)
        result = await self.session.exec(statement)
        return result.first()

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
