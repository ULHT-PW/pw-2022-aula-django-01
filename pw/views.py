from django.shortcuts import render
import datetime

# Create your views here.
def index_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }

    return render(request, 'pw/index.html', context)


def about_view(request):
    return render(request, 'pw/about.html')