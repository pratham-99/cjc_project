from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = []
admin.site.register(Article, ArticleAdmin)
