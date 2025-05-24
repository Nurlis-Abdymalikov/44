from django.urls import path
from . import views


urlpatterns = [
    path('parser_form/', views.ParserForm.as_view(), name='parser_form'),
    path('movie_list/', views.MovieListView.as_view(), name='movie_list')
]