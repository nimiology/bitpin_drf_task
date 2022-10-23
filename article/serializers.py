from djoser.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer

from article.models import Article, ArticleRating


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'rate_length', 'rete_mean')


class ArticleSerializer4ArticleRating(ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'rate_length', 'rete_mean')


class ArticleRatingSerializer(ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = ArticleRating
        fields = ('id', 'owner', 'article', 'rating')

    def to_representation(self, instance):
        self.fields['article'] = ArticleSerializer4ArticleRating()
        return super(ArticleRatingSerializer, self).to_representation(instance)
