from fastapi import FastAPI
from src.app.users import router as user_route
from src.worker.celery_config import celery
from celery.schedules import crontab
app = FastAPI()

app.include_router(user_route.router)


celery.conf.beat_schedule = {
    "run_every_minute": {
        "task": "users.periodic_task",
        "schedule": crontab(minute="*"),
    }
}

if __name__ == '__main__':
    celery.start()