from sqlalchemy import JSON, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'Users'

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    time_register: Mapped[int]
    places_visited: Mapped[list[str]] = mapped_column(JSON, default=list)