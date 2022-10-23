from djoser.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from article.models import Article, ArticleRating


class ArticleSerializer(ModelSerializer):
    user_rate = SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'rate_length', 'rete_mean', 'user_rate']

    def _user(self):
        request = self.context.get('request', None)
        if request:
            if request.user.is_authenticated:
                return request.user
            else:
                return None
        return None

    def get_user_rate(self, instance):
        user = self._user()
        try:
            if user is not None:
                return instance.article_ratings.get(owner=user).rate
            else:
                return None
        except ArticleRating.DoesNotExist:
            return None


class ArticleRatingSerializer(ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = ArticleRating
        fields = ('id', 'owner', 'article', 'rate')

    def save(self, **kwargs):
        owner = kwargs.get('owner')
        article = self.validated_data.get('article')
        try:
            instance = ArticleRating.objects.get(owner=owner, article=article)
            self.instance = instance
        except ArticleRating.DoesNotExist:
            pass
        return super(ArticleRatingSerializer, self).save(**kwargs)

    def to_representation(self, instance):
        self.fields['article'] = ArticleSerializer()
        return super(ArticleRatingSerializer, self).to_representation(instance)
