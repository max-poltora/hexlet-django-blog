from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context = {
        'app_name': 'hexlet-django-blog',
        })

