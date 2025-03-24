from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

BROKER_URL = os.getenv("BROKER_URL", "redis://localhost:6379/0")

celery_app = Celery("translate_tasks", broker=BROKER_URL)
