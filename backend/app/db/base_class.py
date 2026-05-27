from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column

class Base(DeclarativeBase):
  pass

class TimestampMixin:
  created_at = mapped_column(
    DateTime,
    default=datetime.utcnow,
  )

  updated_at = mapped_column(
    DateTime,
    default=datetime.utcnow,
    onupdate=datetime.utcnow,
  )