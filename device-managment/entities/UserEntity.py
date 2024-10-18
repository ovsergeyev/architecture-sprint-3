from database import Base
from sqlalchemy.orm import mapped_column, Mapped

class UserEntity(Base):
  __tablename__ = 'users'

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  name: Mapped[str]