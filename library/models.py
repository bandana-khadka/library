from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    CHAR,
    Date
)


# class Author(Base):
#     __tablename__ = 'authors'
#     id = Column(Integer, primary_key=True)
#     first_name = Column(CHAR(50))
#     last_name = Column(CHAR(50))
#     book_id = ForeignKey(Integer)
#
#
# class BookIssue(Base):
#     __tablename__ = 'book_issues'
#     id = Column(Integer, primary_key=True)
#     book_id = ForeignKey(Integer)
#     user_id = ForeignKey(Integer)
#     issue_date = Column(Date)
#     due_date = Column(Date)
#     status = Column(int)
#
#
# class Book(Base):
#     __tablename__ = 'books'
#     id = Column(Integer, primary_key=True)
#     name = Column(CHAR(50))
#     description = Column(CHAR(200))
#     publication_date = Column(Date)
#     edition = Column(int)
#     publication_address = Column(Date)
#
#
# class UserType(Base):
#     __tablename__ = 'user_types'
#     id = Column(Integer, primary_key=True)
#     type_id = Column(int)
#     type = Column(CHAR(20))
#
#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     first_name = Column(CHAR(50))
#     last_name = Column(CHAR(50))
#     email = Column(CHAR(50))
#     _password = Column(CHAR(100))
#     mobile_number = Column(CHAR(15))
#     type_id = ForeignKey(Integer)


