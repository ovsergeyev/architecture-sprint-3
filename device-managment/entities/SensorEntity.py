from database import Base
from sqlalchemy.orm import mapped_column, Mapped

class SensorEntity(Base):
  __tablename__ = 'sensors'

  serial_number: Mapped[int] = mapped_column(primary_key=True)
  device_id: Mapped[int]