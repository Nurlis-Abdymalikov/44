from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.FilmListView.as_view(), name='films'),
    path('films/<int:id>/', views.FilmDetailView.as_view(), name='film_detail'),  
    path('films/<int:id>/delete/', views.DeleteFilmView.as_view(), name='delete_film'),  
    path('films/<int:id>/update/', views.UpdateFilmView.as_view(), name='update_film'),
    path('create_film/', views.CreateFilmView.as_view(), name='create_film'),  
    path ('search/', views.SearchBookView.as_view(), name='search'),
]
