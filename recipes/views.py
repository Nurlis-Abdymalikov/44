from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .forms import RecipeForm, IngredientForm, IngredientFormSet
from .models import Recipe, Ingredient

class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(generic.CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        ingredients_text = form.cleaned_data.get('ingredients_text', '')

        for line in ingredients_text.splitlines():
            if line.strip():
                parts = line.strip().split(maxsplit=1)
                name = parts[0]
                quantity = parts[1] if len(parts) > 1 else ''
                Ingredient.objects.create(
                    recipe=self.object,
                    name=name,
                    quantity=quantity
                )
        return response

class RecipeDeleteView(generic.DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe-list')
    template_name = 'recipes/recipe_confirm_delete.html' 


