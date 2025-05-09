from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_home_work, name='first_home_work'),
]