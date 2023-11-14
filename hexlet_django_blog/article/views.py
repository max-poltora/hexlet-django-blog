from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic.base import TemplateView
from django.views import View
from .models import Article
from .forms import ArticleForm

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
    
class ArticleFormView(View):
    
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', context = {
                'form': form,
            })
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'article/create.html', context = {
                'form': form,
            })

class ArticleFormEditView(View):
    
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id = article_id)
        form = ArticleForm(instance = article)
        return render(request, 'article/comment.html', context = {
                'form': form,
                'article_id': article_id,
            })
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id = article_id)
        form = ArticleForm(request.POST, instance = article)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'article/comment.html', context = {
                'form': form,
                'article_id': article_id,
            })
    
class ArticleDeleteView(View):
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id = article_id)
        if article:
            article.delete()
        return redirect('articles')