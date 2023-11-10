from django.shortcuts import render, get_object_or_404

from django.views.generic.base import TemplateView
from django.views import View
from .models import Article

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
    
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, 'article/index.html', context = {
                        'articles': articles,
                        })
    
def index(request, tags, article_id):
    return render(request, 'article/article.html', context = {
                      'tags': tags,
                      'article_id': article_id,
                      })

class ArticleView(View):
    
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id = kwargs['id'])
        return render(request, 'article/show.html', context = {
                'article': article,
            })
    