from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("My first page in Django")
