#self created file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request, "index.html")

def about(request):
    return HttpResponse("about")

def removepunc(request):
    return HttpResponse("removepunc")

def charupper(request):
    return HttpResponse("charupper")