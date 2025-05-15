from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse


#update film
def update_film_view(request,id):
    film_id = get_object_or_404(models.Film, id=id)
    if request.method == "POST":
        form  = forms.FilmForm(request.POST, instance=film_id)
        if form.is_valid():
            form.save()
            return HttpResponse('Книга успешно обновлена')
    else:
        form = forms.FilmForm(instance=film_id)
    return render(request, template_name='films/update_film.html', context={
        'form': form,
        'film_id': film_id,
        })


# Delete film
def delete_film_view(request, id):
    film_id = get_object_or_404(models.Film, id=id)
    film_id.delete()
    return HttpResponse('Книга успешно удалена')



#create_book
def create_film_view(request):
    if request.method == 'POST':
        form = forms.FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Фильм успешно добавлена')
    else:
        form = forms.FilmForm()
    return render(request, template_name='films/create_film.html', context={'form': form})

def films_list_view(request):
    if request.method == 'GET':
        films = models.Film.objects.all().order_by('-id')
        context = {
            'films': films,
        }
        return render(request, template_name='films/films.html', context=context)

def film_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(models.Film, id=id)
        context = {
            'film_id': film_id,
        }
        return render(request, 
                      template_name='films/film_detail.html', 
                      context=context)
