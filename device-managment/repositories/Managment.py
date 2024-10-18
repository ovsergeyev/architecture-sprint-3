from sqlalchemy import select, insert, delete, text, update
from database import async_session_maker
from datetime import datetime
from entities import DeviceEntity

class Managment:
  model = DeviceEntity

  @classmethod
  async def add(cls, **data):
    async with async_session_maker() as session:
      query = insert(cls.model).values(**data).returning(cls.model.id)
      await session.execute(query)
      await session.commit()