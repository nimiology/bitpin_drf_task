from django.urls import path

from article.views import ArticleListAPIView

app_name = 'article'
urlpatterns = [
    path('articles/', ArticleListAPIView.as_view(), name='articles_list'),

]