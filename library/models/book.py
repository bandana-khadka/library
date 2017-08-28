from sqlalchemy import (
    Column,
    Integer,
    Date,
    CHAR,
)

from .meta import Base

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(CHAR(50))
    description = Column(CHAR(200))
    publication_date = Column(Date)
    edition = Column(Integer)
    publication_address = Column(Date)
    location = Column(CHAR(20))