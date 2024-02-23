import os
from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Annotated
load_dotenv()

Username = os.getenv("MYSQL_USER")
Password = os.getenv("MYSQL_PASSWORD")
Host = os.getenv("MYSQL_HOST")
database_name = os.getenv("MYSQL_DB")

db_url = f'mysql+pymysql://{Username}:{Password}@localhost:3306/fastapp'

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    except:
        db.rollback()
    finally:
        db.close_all

db_dependancy = Annotated[Session, Depends(get_db)]