from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def upload(request):
    return render(request, 'main/upload.html')


def search(request):
    return render(request, 'main/search.html')


def ajax_search(request):
    search = request.GET["search"]
    return HttpResponse(search)


def ajax_upload(request):
    #this_file = request.POST["firstName"]
    print(request.POST.firstName)
    return HttpResponse('ok')