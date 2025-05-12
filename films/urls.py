from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.films_list_view, name='films'),
    path('films/<int:id>/', views.film_detail_view, name='film_detail'),  
]
