from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'articles'),
    path('<str:tags>/<int:article_id>/', views.index, name = 'article'),
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name = 'article_update'),
    path('<int:id>/delete/', views.ArticleDeleteView.as_view(), name = 'article_delete'),
    path('<int:id>/', views.ArticleView.as_view(), name = 'article_index'),
    path('form/', views.ArticleFormView.as_view(), name = 'article_form')
]