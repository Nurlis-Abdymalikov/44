from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.AllProductsView.as_view(), name = 'all_product'),
    path('meal/', views.MealView.as_view(), name = 'meal_view'),
    path('drink/', views.DrinkView.as_view(), name = 'drink_view'),
]