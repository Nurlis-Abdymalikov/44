from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.films_list_view, name='films'),
    path('films/<int:id>/', views.film_detail_view, name='film_detail'),  
    path('films/<int:id>/delete/', views.delete_film_view, name='delete_film'),  
    path('films/<int:id>/update/', views.update_film_view, name='update_film'),
    path('create_film/', views.create_film_view, name='create_film'),  
]
