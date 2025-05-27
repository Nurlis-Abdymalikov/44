from django.shortcuts import redirect
from django.views import generic
from django.http import HttpResponse
from . import models, forms

class MovieListView(generic.ListView):
    template_name = 'parser_films/parser_film_list.html'
    context_object_name = 'movie'  # это будет содержать page_obj
    model = models.Parser_Movie
    paginate_by = 3  # по 3 фильма на страницу

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = context['page_obj']  # ✅ теперь movie = page_obj
        return context

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
