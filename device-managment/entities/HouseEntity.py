from database import Base
from sqlalchemy.orm import mapped_column, Mapped

class HouseEntity(Base):
  __tablename__ = 'house'

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  user_id: Mapped[int]
  address: Mapped[str]