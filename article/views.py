from rest_framework.generics import ListAPIView

from article.models import Article
from article.serializers import ArticleSerializer


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = {'title': ['exact', 'contains'],
                        'text': ['exact', 'contains'],

                        }
    ordering_fields = ['id', 'title', 'text', '?']

