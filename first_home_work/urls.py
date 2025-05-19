from django.urls import path
from . import views

urlpatterns = [
    path('', views.FirstHomeWorkView.as_view(), name='first_home_work'),
]