from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
    CHAR,
    Date,
    Table
)

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(CHAR(50))
    last_name = Column(CHAR(50))
    book_id = ForeignKey(Integer)

ideas_tags = Table('authors', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id'))
)

class BookIssue(Base):
    __tablename__ = 'book_issues'
    id = Column(Integer, primary_key=True)
    book_id = ForeignKey(Integer)
    user_id = ForeignKey(Integer)
    issue_date = Column(Date)
    due_date = Column(Date)
    status = Column(int)

#issued_books = Table('book_issues', Base.metadata,
#    Column('book_id', Integer, ForeignKey('books.id')),
#    Column('user_id', Integer, ForeignKey('users.id'))
#)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(CHAR(50))
    description = Column(CHAR(200))
    publication_date = Column(Date)
    edition = Column(int)
    publication_address = Column(Date)

class UserType(Base):
    __tablename__ = 'user_types'
    id = Column(Integer, primary_key=True)
    type_id = Column(int)
    type = Column(CHAR(20))

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(CHAR(50))
    last_name = Column(CHAR(50))
    email = Column(CHAR(50))
    _password = Column(CHAR(100))
    mobile_number = Column(CHAR(15))
    type_id = ForeignKey(Integer)

#ideas_tags = Table('users', Base.metadata,
#    Column('type_id', Integer, ForeignKey('user_types.id'))
#)

