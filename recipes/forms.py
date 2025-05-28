from django import forms
from .models import Recipe, Ingredient
from django.forms import modelformset_factory

class RecipeForm(forms.ModelForm):
    ingredients_text = forms.CharField(
        label="Ингредиенты",
        widget=forms.Textarea(attrs={'rows': 5}),
        required=False
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients_text']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']

IngredientFormSet = modelformset_factory(Ingredient, form=IngredientForm, extra=1)
