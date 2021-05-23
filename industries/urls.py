from django.urls import path
from . import views

urlpatterns = [
    path('industry', views.getAllIndustries, name = 'getAllIndustries'),
    path('industry/specfic', views.getIndustry, name = 'getIndustry'),
    path('industry/', views.getIndustry, name = 'getIndustry'),
]