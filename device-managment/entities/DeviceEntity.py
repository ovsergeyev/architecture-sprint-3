from database import Base
from sqlalchemy.orm import mapped_column, Mapped
from typing import Optional

class DeviceEntity(Base):
  __tablename__ = 'devices'

  serial_number: Mapped[str] = mapped_column(primary_key=True)
  status: Mapped[Optional[bool]]