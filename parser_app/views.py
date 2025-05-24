from django.shortcuts import redirect
from django.views import generic
from django.http import HttpResponse
from . import models, forms

class MovieListView(generic.ListView):
    template_name = 'parser_films/parser_film_list.html'
    context_object_name = 'movie'
    model = models.Parser_Movie

    def get_queryset(self):
        return self.model.objects.all()

class ParserForm(generic.FormView):
    template_name = 'parser_films/parser_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Парсинг успешно завершен!!!</h1>')
        else:
            return super(ParserForm, self).post(request, *args, **kwargs)