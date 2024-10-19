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
      query = insert(cls.device_model).values(**data).returning(cls.device_model.serial_number)
      result = await session.execute(query)
      await session.commit()
      return result.mappings().one_or_none()

  @classmethod
  async def add_sensor(cls, data):
    async with async_session_maker() as session:
      query = insert(cls.sensor_model).values(**data).returning(cls.sensor_model.serial_number)
      result = await session.execute(query)
      await session.commit()
      return result.mappings().one_or_none()

  @classmethod
  async def find_sensor_by_serial_number(cls, serial_number):
    async with async_session_maker() as session:
      query = select(cls.sensor_model.__table__.columns).filter_by(serial_number=serial_number)
      result = await session.execute(query)
      return result.mappings().one_or_none()

  @classmethod
  async def update_sensor(cls, data):
    async with async_session_maker() as session:
      try:
        query = update(cls.sensor_model).where(cls.sensor_model.serial_number==data['serial_number']).values(**data)
        await session.execute(query)
        await session.commit()
        return True
      except:
        return False

  @classmethod
  async def find_device_by_serial_number(cls, serial_number):
    async with async_session_maker() as session:
      query = select(cls.device_model.__table__.columns).filter_by(serial_number=serial_number)
      result = await session.execute(query)
      return result.mappings().one_or_none()

  @classmethod
  async def update_device(cls, data):
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
      query = insert(cls.target_temperature_model).values(**data).returning(cls.target_temperature_model.device_id)
      await session.execute(query)
      await session.commit()

  @classmethod
  async def find_target_temperature_by_device_id(cls, device_id):
    async with async_session_maker() as session:
      query = select(cls.target_temperature_model.__table__.columns).filter_by(device_id=device_id)
      result = await session.execute(query)
      return result.mappings().one_or_none()

  @classmethod
  async def update_target_temperature(cls, data):
    async with async_session_maker() as session:
      try:
        query = update(cls.target_temperature_model).where(cls.target_temperature_model.device_id==data['device_id']).values(**data)
        await session.execute(query)
        await session.commit()
        return True
      except:
        return False

