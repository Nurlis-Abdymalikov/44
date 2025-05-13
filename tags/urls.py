from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products_view, name = 'all_product'),
    path('meal/', views.meal_view, name = 'meal_view'),
    path('drink/', views.drink_view, name = 'drink_view'),
]