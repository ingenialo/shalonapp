from apps.taskapp.celery import app
from apps.payments.models import Payment

from apps.payments.services import getPaymentsFromAgendaPro
# Utilities
import datetime
import pytz

@app.task(name='get_agenda_pro_payments_for_today', max_retries=3)
def get_agenda_pro_payments_for_today():
    """get_agenda_pro_payments_for_today"""
    colombian_timezone = pytz.timezone("America/Bogota") 
    now = datetime.datetime.now(colombian_timezone)
    today = now.strftime('%y-%m-%d')
    print("-------------------get_agenda_pro_payments_for_today--------------")
    print(today)
    getPaymentsFromAgendaPro(today)
