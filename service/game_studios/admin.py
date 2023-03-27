from django.contrib import admin

from .models import Publisher, Developer


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    """Game publisher admin model"""
    list_display = ('name', 'slug')


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    """Game developer admin model"""
    list_display = ('name', 'slug')
