#views.py

from .models import School
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView

class SchoolListView(ListView):
    model = School
    template_name = 'basic_app/index.html'
    context_object_name = 'schools'

    def get_queryset(self):
        #return School.objects.filter(location__contains='New York')
        return School.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SchoolListView, self).get_context_data()
        context['some_data'] = 'This is some other data'
        return context


class SchoolDetailView(DetailView):
    model = School
