from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse
from django.views import generic
from django.db.models import F



#search
class SearchBookView(generic.ListView):
    template_name = 'films/films.html'
    context_object_name = 'film'
    paginate_by = 5
    model = models.Film

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context





class UpdateFilmView(generic.UpdateView):
    template_name= 'films/update_film.html'
    form_class = forms.FilmForm
    success_url = '/films/'

    def get_object(self, *agrs, **kwargs ):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.Film, id=film_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateFilmView, self).form_valid(form=form)

# #update film
# def update_film_view(request,id):
#     film_id = get_object_or_404(models.Film, id=id)
#     if request.method == "POST":
#         form  = forms.FilmForm(request.POST, instance=film_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Книга успешно обновлена')
#     else:
#         form = forms.FilmForm(instance=film_id)
#     return render(request, template_name='films/update_film.html', context={
#         'form': form,
#         'film_id': film_id,
#         })




class DeleteFilmView(generic.DeleteView):
    template_name = 'films/confirm_delete.html'
    success_url = '/films/'

    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.Film, id=film_id)


# Delete film
# def delete_film_view(request, id):
#     film_id = get_object_or_404(models.Film, id=id)
#     film_id.delete()
#     return HttpResponse('Книга успешно удалена')


class CreateFilmView(generic.CreateView):
    template_name='films/create_film.html'
    form_class = forms.FilmForm
    success_url = '/films/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateFilmView, self).form_valid(form=form)


# #create_book
# def create_film_view(request):
#     if request.method == 'POST':
#         form = forms.FilmForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Фильм успешно добавлена')
#     else:
#         form = forms.FilmForm()
#     return render(request, template_name='films/create_film.html', context={'form': form})


class FilmListView(generic.ListView):
    template_name = 'films/films.html'
    model = models.Film
    paginate_by = 3

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


# def films_list_view(request):
#     if request.method == 'GET':
#         films = models.Film.objects.all().order_by('-id')
#         context = {
#             'films': films,
#         }
#         return render(request, template_name='films/films.html', context=context)



class FilmDetailView(generic.DetailView):
    template_name = 'films/film_detail.html'
    model = models.Film
    pk_url_kwarg = 'id'  

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        film = self.object
        viewed_films = request.session.get("viewed_films", [])
        if film.id not in viewed_films:
            film.views = F("views") + 1
            film.save()
            film.refresh_from_db()

            viewed_films.append(film.id)
            request.session["viewed_films"] = viewed_films
        return response


# def film_detail_view(request, id):
#     if request.method == 'GET':
#         film_id = get_object_or_404(models.Film, id=id)
#         context = {
#             'film_id': film_id,
#         }
#         return render(request, 
#                       template_name='films/film_detail.html', 
#                       context=context)
    