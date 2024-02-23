from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db_config import Base, engine

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String(length=30), nullable=False)
    password = Column(String(length=20), nullable=False)

class Posts(Base):

    __tablename__ = 'user_posts'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String(length=100), nullable=True)
    user_id = Column(ForeignKey("users.id"))


Base.metadata.create_all(engine)