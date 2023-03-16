from django.contrib import admin

from .models import Article, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Article admin model"""
    list_display = ('title', 'slug', 'created_at', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Article tag admin model"""
    list_display = ('name', 'slug', )
