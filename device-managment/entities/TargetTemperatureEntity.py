from database import Base
from sqlalchemy.orm import mapped_column, Mapped

class TargetTemperatureEntity(Base):
  __tablename__ = 'target_temperatures'

  device_id: Mapped[str] = mapped_column(primary_key=True)
  temperature: Mapped[float]