from django.shortcuts import render
from django.views import generic

class FirstHomeWorkView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emoji'] = "🤠"
        context['text'] = 'Привет, надеюсь, этот проект запустится'
        context['run_string'] = 'RY RY RY'
        return context

# def first_home_work(request):
#     if request.method == 'GET':
#         context = {
#             'emoji':"🤠",
#             'text':'Привет надеюсь этот проект запуститься',
#             'run_string':'RY RY RY',
#         }
#         return render(request, template_name='index.html',context=context)
