from django.shortcuts import render
from django.views.generic.base import TemplateView

'''
def index(request):
    return render(request, 'article/index.html', context = {
        'app_name': 'hexlet-django-blog',
        })
'''

class IndexView(TemplateView):
    
    template_name = 'article/index.html'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'hexlet-django-blog'
        
        return context