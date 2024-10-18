from database import Base
from sqlalchemy.orm import mapped_column, Mapped

class SensorEntity(Base):
  __tablename__ = 'sensors'

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  device_id: Mapped[int]