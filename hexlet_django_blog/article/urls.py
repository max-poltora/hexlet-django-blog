from django.urls import path

from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleFormView, ArticleFormEditView

urlpatterns = [
    path('', IndexView.as_view(), name = 'articles'),
    path('<str:tags>/<int:article_id>/', views.index, name = 'article'),
    path('<int:id>/edit', ArticleFormEditView.as_view(), name = 'article_update'),
    path('<int:id>/', ArticleView.as_view(), name = 'article_index'),
    path('form/', ArticleFormView.as_view(), name = 'article_form')
]