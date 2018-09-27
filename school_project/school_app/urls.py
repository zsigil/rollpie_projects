from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('school/<int:pk>/', views.SchoolDetailView.as_view(), name='school_detail'),
]
