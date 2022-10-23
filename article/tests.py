from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from article.models import Article, ArticleRating


def get_user_token(username):
    user = get_user_model().objects.create(username=username, password='test')
    refresh = RefreshToken.for_user(user)
    return user, f'Bearer {refresh.access_token}'


class ArticleAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user, self.token = get_user_token('test')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        self.article = Article.objects.create(title='test', text='test')
        self.rating = ArticleRating.objects.create(article=self.article, owner=self.user, rate='5')

    def test_get_articles_list(self):
        response = self.client.get(reverse('article:articles_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_serializer_fields(self):
        response = self.client.get(reverse('article:articles_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['rate_length'], self.article.rate_length())
        self.assertEqual(response.data['results'][0]['rete_mean'], self.article.rete_mean())
        self.assertEqual(response.data['results'][0]['user_rate'], '5')


class ArticleRatingAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user, self.token = get_user_token('test1')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        self.article = Article.objects.create(title='test', text='test')
        self.rating = ArticleRating.objects.create(article=self.article, owner=self.user, rate='5')

    def test_update_article(self):
        response = self.client.post(reverse('article:rating'), data={'article': self.article.pk, 'rate': '4'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['id'], self.rating.pk)
        self.assertEqual(response.data['rate'], '4')

    def test_create_article(self):
        self.user, self.token = get_user_token('test2')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        response = self.client.post(reverse('article:rating'), data={'article': self.article.pk, 'rate': '2'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['rate'], '2')
