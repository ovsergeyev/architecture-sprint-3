from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import DateTime
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime

from config import settings

engine = create_async_engine(settings.DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
  pass
  # created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
  # updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)