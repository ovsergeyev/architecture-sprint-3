from database import Base
from sqlalchemy.orm import mapped_column, Mapped
from typing import Optional

class DeviceEntity(Base):
  __tablename__ = 'devices'

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  serial_number: Mapped[str]
  status: Mapped[Optional[bool]]