from django.contrib import admin

from article.models import ArticleRating, Article


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ("title", "text",)
    search_fields = ("title", "text")


class ArticleRatingModelAdmin(admin.ModelAdmin):
    list_display = ("owner", "article", "rate")
    list_filter = ("rate", )
    search_fields = list_display


admin.site.register(Article, ArticleModelAdmin)
admin.site.register(ArticleRating, ArticleRatingModelAdmin)
