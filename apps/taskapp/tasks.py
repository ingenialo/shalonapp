# Celery
from apps.taskapp.celery import app
from celery.schedules import crontab

import time

@app.task(name='test_task', max_retries=3)
def test_task():
    for i in range(5):
        time.sleep(1)
        print("sleeping", str(i+1))


app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'get_agenda_pro_payments_for_today',
        'schedule': crontab(hour=5, minute=30),
    },
}