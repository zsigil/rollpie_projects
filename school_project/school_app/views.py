from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import School

def index(request):
    schools = School.objects.all()
    context = {'schools':schools}
    return render(request, 'school_app/schools.html', context)

class SchoolDetailView(DetailView):
    model = School
    template_name = 'school_app/school_detail.html'
