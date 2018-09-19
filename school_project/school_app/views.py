from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'school_app/schools.html', context)
