from django.contrib import admin
from django.forms import TextInput
from django.db import models
from django.utils.safestring import mark_safe

from .models import (
    Item,
    Tag,
    Customer,
    Favorite,
    ItemScreenshot,
    ItemDiscount,
    ItemPlatform
)

admin.site.site_header = "Pixel Playground | Administration"


class ItemScreenshotInLine(admin.TabularInline):
    """Item screenshots in line admin model"""
    model = ItemScreenshot


# class ItemPlatformInLine(admin.TabularInline):
#     """Item screenshots in line admin model"""
#     model = Item.platforms.through


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_price', 'currency', 'get_tags', 'slug',  'get_poster', )
    list_editable = ('currency', )
    search_fields = ('name', )

    inlines = [
        ItemScreenshotInLine,
        # ItemPlatformInLine
    ]

    class Media:
        css = {
            'all': ('css/admin-panel-styles.css',)
        }

    def get_poster(self, obj=None):
        if obj.poster:
            return mark_safe(f"<img src={obj.poster.url} width='50' height='auto' object-fit='cover'")
        else:
            pass



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag admin model"""
    list_display = ('name', 'slug', )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Customer admin model"""
    pass


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Favorite admin model"""
    pass


@admin.register(ItemDiscount)
class ItemDiscountAdmin(admin.ModelAdmin):
    """Favorite admin model"""
    pass


@admin.register(ItemPlatform)
class ItemDiscountAdmin(admin.ModelAdmin):
    """Favorite admin model"""
    list_display = ('name', 'slug')


