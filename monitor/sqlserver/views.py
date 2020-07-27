from django.http import HttpResponse
import time
from .models import *

from django.template import loader

ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# ticks=time.time()

def index(request):
    ##example 1
    # latest_backup = backup_test.objects.order_by('start_date')[:5]
    # output = '</br>'.join([str(q.id) for q in latest_backup])
    # return HttpResponse('当前的备份：</br>'+output)

    latest_backup_list = backup_test.objects.order_by('start_date')[:40]
    template = loader.get_template('sqlserver/index.html')
    context = {
        'latest_backup_list': latest_backup_list,

    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    return HttpResponse("You're looking at question %s." % id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)