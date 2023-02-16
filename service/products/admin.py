from django.contrib import admin
from django.forms import TextInput
from django.db import models

from .models import Item, Order, Tag

admin.site.site_header = "Game Store administration"


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_price', 'currency', 'get_tags')
    list_editable = ('currency', )

    class Media:
        css = {
            'all': ('css/admin-panel-styles.css',)
        }


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Order admin model"""
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag admin model"""
    pass
