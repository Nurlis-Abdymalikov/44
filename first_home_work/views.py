from django.shortcuts import render

def first_home_work(request):
    if request.method == 'GET':
        context = {
            'emoji':"🤠",
            'text':'Привет надеюсь этот проект запуститься',
            'run_string':'RY RY RY',
        }
        return render(request, template_name='index.html',context=context)
