from django.contrib.auth import get_user_model
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title

    def rate_length(self):
        return len(self.article_ratins.all())

    def rete_mean(self):
        ratings = self.article_ratins.all()
        rates_sum = sum(rate.rate for rate in ratings)
        return rates_sum / len(ratings)


class ArticleRating(models.Model):
    related_name = 'article_ratings'
    RATE_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name=related_name)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name=related_name)
    rate = models.CharField(max_length=1, choices=RATE_CHOICES)

    class Meta:
        unique_together = ('owner', 'article')

    def __str__(self):
        return f'{self.owner.username} - {self.article.title}'
