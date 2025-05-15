from django import forms
from . import models 

class FilmForm(forms.ModelForm):
    class Meta:
        model = models.Film
        fields = '__all__'