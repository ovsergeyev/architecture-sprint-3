from database import Base
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime

class TelemetryEntity(Base):
  __tablename__ = 'telemetries'

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  datetime: Mapped[datetime]
  sensor_id: Mapped[int]
  data: Mapped[str]