from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    CHAR,
    ForeignKey,
)

from .meta import Base

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(CHAR(50))
    last_name = Column(CHAR(50))
    book_id = Column(Integer)