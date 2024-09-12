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

    async def create_sample(self, sample_create_data: SampleCreateModel):
        """
        Creates a new sample in the database

        Args:
            sample_create_data (SampleCreateModel): data to create a new sample

        Returns:
            Samples: a new sample
        """
        new_sample = Samples(**sample_create_data.model_dump())
        self.session.add(new_sample)
        await self.session.commit()
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
