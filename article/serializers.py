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

    # def get_rate_length(self):
    #     return len(self.instance.article_ratins.all())
    #
    # def get_rete_mean(self):
    #     ratings = self.instance.article_ratins.all()
    #     rates_sum = sum(rate.rate for rate in ratings)
    #     return rates_sum / len(ratings)


class ArticleRatingSerializer(ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = ArticleRating
        fields = ('id', 'owner', 'article', 'rating')

    def to_representation(self, instance):
        self.fields['article'] = ArticleSerializer()
        return super(ArticleRatingSerializer, self).to_representation(instance)
