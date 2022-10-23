from django.urls import path

from article.views import ArticleListAPIView, ArticleRatingAPIView

app_name = 'article'
urlpatterns = [
    path('articles/', ArticleListAPIView.as_view(), name='articles_list'),

    path('rating/', ArticleRatingAPIView.as_view(), name='rating'),
]