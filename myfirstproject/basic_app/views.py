#views.py

from django.shortcuts import render
from .models import School

def index(request):
    schools = School.objects.all()
    return render(request, 'basic_app/index.html', {'schools':schools})
