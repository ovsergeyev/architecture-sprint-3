from database import Base
from sqlalchemy.orm import mapped_column, Mapped

class TargetTemperatureEntity(Base):
  __tablename__ = 'target_temperatures'

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  device_id: Mapped[str]
  temperature: Mapped[float]