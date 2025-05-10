from django.shortcuts import render
from . import models

def films_list_view(request):
    if request.method == 'GET':
        films = models.Film.objects.all().order_by('-id')
        context = {
            'films': films,
        }
        return render(request, template_name='films/films.html', context=context)
