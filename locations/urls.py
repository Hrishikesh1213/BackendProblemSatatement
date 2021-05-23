from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('location', views.getAllLocations, name = 'getAllLocations'),
    path('location/specfic', views.getLocation, name = 'getLocation'),
    path('location/', views.getLocation, name = 'getLocation'),
]