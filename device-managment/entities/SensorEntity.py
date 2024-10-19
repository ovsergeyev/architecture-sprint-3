from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from schemas.SDevice import SDevice

class SensorEntity(Base):
  __tablename__ = 'sensors'

  serial_number: Mapped[str] = mapped_column(primary_key=True)
  device_id: Mapped[str] = mapped_column(ForeignKey('devices.serial_number'))