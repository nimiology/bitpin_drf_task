from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from article.models import Article, ArticleRating
from article.serializers import ArticleSerializer, ArticleRatingSerializer


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = {'title': ['exact', 'contains'],
                        'text': ['exact', 'contains']
                        }
    ordering_fields = ['id', 'title', 'text', '?']


class ArticleRatingAPIView(CreateAPIView):
    queryset = ArticleRating.objects.all()
    serializer_class = ArticleRatingSerializer
    filterset_fields = {'article': ['exact'],
                        'owner': ['exact'],
                        'rate': ['exact'],
                        }
    ordering_fields = ['id', 'title', 'text', '?']

    def post(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # add owner from request user
        return serializer.save(owner=self.request.user)
