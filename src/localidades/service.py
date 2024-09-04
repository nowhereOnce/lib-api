from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import Localidades
from .schemas import LocalidadCreateModel
from sqlmodel import select


class LocalidadService:
    """
    Esta clase provee los metodos para crear, leer, actualizar, y eliminar localidades
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_localidades(self):
        """
        Obtiene una lista con todas las localidades

        Returns:
            list: una lista de localidades
        """
        statement = select(Localidades).order_by(Localidades.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def create_localidad(self, localidad_create_data: LocalidadCreateModel):
        """
        Crea una nueva localidad en la base de datos

        Args:
            localidad_create_data (LocalidadCreateModel): data para crear una nueva localidad

        Returns:
            Localidad: una nueva localidad
        """
        new_localidad = Localidades(**localidad_create_data.model_dump())
        self.session.add(new_localidad)
        await self.session.commit()
        return new_localidad

    async def get_localidad(self, localidad_uid: str):
        """Obtiene una localidad por su UUID.

        Args:
            localidad_uid (str): el UUID de la localidad

        Returns:
            Localidades: un objeto localidad
        """
        statement = select(Localidades).where(Localidades.uid == localidad_uid)
        result = await self.session.exec(statement)
        return result.first()

    async def update_localidad(self, localidad_uid: str, localidad_update_data: LocalidadCreateModel):
        """Actualiza una localidad

        Args:
            localidad_uid (str): el UUID de la localidad
            localidad_update_data (LocalidadCreateModel): la data para actualizar la localidad

        Returns:
            Localidades: la localidad actualizada
        """

        statement = select(Localidades).where(Localidades.uid == localidad_uid)
        result = await self.session.exec(statement)
        localidad = result.first()
        for key, value in localidad_update_data.model_dump().items():
            setattr(localidad, key, value)
        await self.session.commit()
        return localidad

    async def delete_localidad(self, localidad_uid):
        """Borra una localidad

        Args:
            localidad_uid (str): el UUID de la localidad
        """
        statement = select(Localidades).where(Localidades.uid == localidad_uid)
        result = await self.session.exec(statement)
        localidad = result.first()
        await self.session.delete(localidad)
        await self.session.commit()
