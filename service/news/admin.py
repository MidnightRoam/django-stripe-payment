from django.contrib import admin

from .models import (
    Article,
    Tag,
    Error,
    Url
)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Article admin model"""
    list_display = ('title', 'slug', 'created_at', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Article tag admin model"""
    list_display = ('name', 'slug', )


@admin.register(Error)
class ErrorAdmin(admin.ModelAdmin):
    """Parsing error admin model"""
    list_display = ('data', 'timestamp')


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    """Parsing error admin model"""
    pass
