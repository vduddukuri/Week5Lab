from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {"Message": "Hello World!"})
