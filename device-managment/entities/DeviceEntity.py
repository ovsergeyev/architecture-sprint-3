from database import Base
from sqlalchemy.orm import mapped_column, Mapped

class DeviceEntity(Base):
  __tablename__ = 'devices'

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  status: Mapped[bool]