from django.urls import path
from .views import RecipeCreateView, RecipeListView, RecipeDetailView, RecipeDeleteView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe-add'), 
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
]
