from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

salary_small = "зарплата 10 000 сом"
salary_normal = "зарплата 50 000 сом"
salary_big = "зарплата 100 000 сом"

class ExperienceMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = int(request.POST.get('experience'))
            if experience < 1:
                return HttpResponseBadRequest('sorry, we can not accept you')
            elif experience >= 1 and experience< 3:
                request.salary = salary_small
            elif experience >= 3 and experience < 5:
                request.salary = salary_normal
            elif experience >= 5 and experience <= 10:
                request.salary = salary_big
            else:
                return HttpResponseBadRequest('Вы слишком опытны вам это покажется скучным')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'salary', 'зарплата не определена')