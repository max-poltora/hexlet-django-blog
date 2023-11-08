from django.shortcuts import render, redirect
from django.urls import reverse
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
    
def index(request, tags, article_id):
    return render(request, 'article/article.html', context = {
                      'tags': tags,
                      'article_id': article_id,
                      })