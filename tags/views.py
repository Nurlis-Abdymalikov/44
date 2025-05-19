from django.shortcuts import render
from . import models
from django.views import generic


class AllProductsView(generic.ListView):
    template_name = 'tags/all_products.html'
    context_object_name = 'all_products'
    queryset = models.Product.objects.all().order_by('-id')

# def all_products_view(request):
#     if request.method == 'GET':
#         all_products = models.Product.objects.all().order_by('-id')
#         context = {
#             'all_products':all_products,
#         }
#         return render(request, template_name="tags/all_products.html", context=context)


class MealView(generic.ListView):
    template_name = 'tags/meals.html'
    context_object_name = 'meal'

    def get_queryset(self):
        return models.Product.objects.filter(tags__name='#Еда').order_by('-id')



# def meal_view(request):
#     if request.method == 'GET':
#         meal = models.Product.objects.all().order_by('-id').filter(tags__name ='#Еда')
#         context = {
#             'meal':meal,
#         }
#         return render(request, template_name="tags/meals.html", context=context)
    


class DrinkView(generic.ListView):
    template_name = 'tags/drinks.html'
    context_object_name = 'drink'

    def get_queryset(self):
        return models.Product.objects.filter(tags__name='#Напитки').order_by('-id')


# def drink_view(request):
#     if request.method == 'GET':
#         drink = models.Product.objects.all().order_by('-id').filter(tags__name ='#Напитки')
#         context = {
#             'drink':drink,
#         }
#         return render(request, template_name="tags/drinks.html", context=context)