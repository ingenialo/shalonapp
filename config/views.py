# Django
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Tasks
from apps.taskapp.tasks import test_task

# @login_required
def test_celery(request):
    test_task.delay()
    return HttpResponse("task executed correctly!")

def home(request):
    return HttpResponseRedirect("/admin")