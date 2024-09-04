from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import Muestras, Rocas, Localidades
from .schemas import MuestraCreateModel
from sqlmodel import select


class MuestraService:
    """
    Esta clase provee los metodos para crear, leer, actualizar, y eliminar muestras
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    # Pendiente: Intentar realizar la siguiente consulta de SQL:
    # SELECT 
    # m.*,  -- Todos los campos de Muestras
    # r.nombre AS nombre_roca,  -- Información de Rocas
    # l.nombre AS nombre_localidad  -- Información de Localidades
    # FROM 
    #     muestras m
    # JOIN 
    #     rocas r ON m.roca_uid = r.uid  -- Relaciona Muestras con Rocas
    # JOIN 
    #     localidades l ON m.localidad_uid = l.uid;  -- Relaciona Muestras con Localidades

    async def get_all_muestras(self):
        """
        Obtiene una lista con todas las muestras

        Returns:
            list: una lista de muestras
        """
        statement = select(Muestras).order_by(Muestras.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def create_muestra(self, muestra_create_data: MuestraCreateModel):
        """
        Crea una nueva muestra en la base de datos

        Args:
            muestra_create_data (MuestraCreateModel): data para crear una nueva muestra

        Returns:
            Muestras: una nueva muestra
        """
        new_muestra = Muestras(**muestra_create_data.model_dump())
        self.session.add(new_muestra)
        await self.session.commit()
        return new_muestra

    async def get_muestra(self, muestra_uid: str):
        """Obtiene una muestra por su UUID.

        Args:
            muestra_uid (str): el UUID de la muestra

        Returns:
            Muestras: un objeto muestra
        """
        statement = select(Muestras).where(Muestras.uid == muestra_uid)
        result = await self.session.exec(statement)
        return result.first()

    async def update_muestra(self, muestra_uid: str, muestra_update_data: MuestraCreateModel):
        """Actualiza una muestra

        Args:
            muestra_uid (str): el UUID de la muestra
            muestra_update_data (MuestraCreateModel): la data para actualizar la muestra

        Returns:
            Muestras: la muestra actualizada
        """

        statement = select(Muestras).where(Muestras.uid == muestra_uid)
        result = await self.session.exec(statement)
        muestra = result.first()
        for key, value in muestra_update_data.model_dump().items():
            setattr(muestra, key, value)
        await self.session.commit()
        return muestra

    async def delete_muestra(self, muestra_uid):
        """Borra una muestra

        Args:
            muestra_uid (str): el UUID de la muestra
        """
        statement = select(Muestras).where(Muestras.uid == muestra_uid)
        result = await self.session.exec(statement)
        muestra = result.first()
        await self.session.delete(muestra)
        await self.session.commit()
