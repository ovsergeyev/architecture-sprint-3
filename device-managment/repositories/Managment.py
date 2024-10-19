from sqlalchemy import select, insert, delete, text, update
from database import async_session_maker
from datetime import datetime
from entities.DeviceEntity import DeviceEntity
from entities.HouseEntity import HouseEntity
from entities.SensorEntity import SensorEntity
from entities.TargetTemperatureEntity import TargetTemperatureEntity
from entities.UserEntity import UserEntity

class Managment:
  device_model = DeviceEntity
  house_model = HouseEntity
  sensor_model = SensorEntity
  target_temperature_model = TargetTemperatureEntity
  user_model = UserEntity

  @classmethod
  async def add_device(cls, data):
    async with async_session_maker() as session:
      query = insert(cls.device_model).values(**data).returning(cls.device_model.id)
      await session.execute(query)
      await session.commit()

  @classmethod
  async def find_device(cls, **filter_by):
    async with async_session_maker() as session:
      query = select(cls.device_model.__table__.columns).filter_by(**filter_by)
      result = await session.execute(query)
      return result.mappings().one_or_none()

  @classmethod
  async def update_device_by_serial_number(cls, data):
    async with async_session_maker() as session:
      try:
        query = update(cls.device_model).where(cls.device_model.serial_number==data['serial_number']).values(**data)
        await session.execute(query)
        await session.commit()
        return True
      except:
        return False

  @classmethod
  async def add_target_temperature(cls, data):
    async with async_session_maker() as session:
      query = insert(cls.target_temperature_model).values(**data).returning(cls.target_temperature_model.id)
      await session.execute(query)
      await session.commit()
