from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("This is home")

def about(request):
    return HttpResponse("This is about")

def contact(request):
    return HttpResponse("This is contact")