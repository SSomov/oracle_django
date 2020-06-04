from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
import json
import csv
from .models import TestDjango

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def upload(request):
    return render(request, 'main/upload.html')


def search(request):
    return render(request, 'main/search.html')


def ajax_search(request):
    search = request.GET["search"]
    obj = TestDjango.objects.filter(id=search).first()
    mess = "DATA_LOAD "+obj.data_load+"<br>"+"SENDER "+obj.sender+"<br>"+"RECEIVER "+obj.receiver
    return HttpResponse(mess)


def ajax_upload(request):
    # req = json.loads(request.body.decode('utf-8'))
    # print(req, type(req))
    x = handle_uploaded_file(request.FILES['file'])
    return HttpResponse(x)


def handle_uploaded_file(f):
    with open('media/temp.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    with open('media/temp.csv', "r", encoding='utf-8') as csvbase:
        spamreader = csv.reader(csvbase, delimiter=';')
        for lines in spamreader:
            TestDjango.objects.filter(msg_id=lines[0]).update(
                update_status=lines[1],
                update_user=lines[2]
            )
        return "ok"
