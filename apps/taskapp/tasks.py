# Celery
from apps.taskapp.celery import app
from celery.decorators import periodic_task

# Utilities
from datetime import timedelta, timezone

import time

@app.task(name='test_task', max_retries=3)
def test_task():
    for i in range(5):
        time.sleep(1)
        print("sleeping", str(i+1))

# @periodic_task(name='get_agenda_pro_payments', run_every=timedelta(seconds=5))
# def get_agenda_pro_payments():
#     """get_agenda_pro_payments"""
#     now = timezone.now()
#     print(now)