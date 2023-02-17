from django.contrib import admin
from django.forms import TextInput
from django.db import models
from django.utils.safestring import mark_safe

from .models import Item, Order, Tag, Customer

admin.site.site_header = "Game Store administration"


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_price', 'currency', 'get_tags', 'get_poster')
    list_editable = ('currency', )

    class Media:
        css = {
            'all': ('css/admin-panel-styles.css',)
        }

    def get_poster(self, obj=None):
        if obj.poster:
            return mark_safe(f"<img src={obj.poster.url} width='50' height='auto' object-fit='cover'")
        else:
            pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Order admin model"""
    list_display = ('id', 'customer', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag admin model"""
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Customer admin model"""
    pass
