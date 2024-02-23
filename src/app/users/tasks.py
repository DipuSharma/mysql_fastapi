import os
from src.worker.celery_config import celery
from sqlalchemy.orm.session import Session
from fastapi import Depends
news_url = os.getenv("News_url")
api_key = os.getenv("News_api_key")

@celery.task()
def periodic_task():
    get_record = news_url+api_key
