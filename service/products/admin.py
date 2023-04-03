from django.contrib import admin
from django.forms import TextInput
from django.db import models
from django.utils.safestring import mark_safe

from .models import (
    Item,
    Tag,
    Genre,
    Customer,
    Favorite,
    ItemScreenshot,
    GameTrailer,
    ItemDiscount,
    ItemPlatform,
    ItemDLC,
    Language,
    ItemLocalization,
    MinimalSystemRequirements,
    RegionOfActivation,
    Region,
)

admin.site.site_header = "Pixel Playground | Administration"


class ItemScreenshotInline(admin.TabularInline):
    """Item screenshots in line admin model"""
    model = ItemScreenshot


class GameTrailerInline(admin.TabularInline):
    """Game trailers in line admin model"""
    model = GameTrailer
    extra = 0


class ItemLocalizationInline(admin.TabularInline):
    """Item localization in line admin model"""
    model = ItemLocalization
    extra = 0


class MinimalSystemRequirementsInline(admin.TabularInline):
    """MinimalSystemRequirements in line admin model"""
    model = MinimalSystemRequirements
    extra = 0


class RegionOfActivationInline(admin.TabularInline):
    """MinimalSystemRequirements in line admin model"""
    model = RegionOfActivation
    extra = 0


@admin.register(ItemDLC)
class ItemDLCAdmin(admin.ModelAdmin):
    """Item screenshots in line admin model"""
    model = ItemDLC


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_price', 'currency', 'amount', 'slug',  'get_poster', )
    list_editable = ('currency', 'amount')
    search_fields = ('name', )

    inlines = [
        ItemScreenshotInline,
        ItemLocalizationInline,
        MinimalSystemRequirementsInline,
        RegionOfActivationInline,
        GameTrailerInline,
    ]

    # fieldsets = (
    #     ('Product info', {
    #         'fields': (('name', 'tagline',), 'description', 'poster', 'trailer')
    #     }),
    #     ('Product price', {
    #         'fields': (('price', 'currency',), 'amount')
    #     }),
    #     ('Product tags and platform of activation', {
    #         'fields': ('tags', 'platform',)
    #     }),
    #     ('Publisher & Developer', {
    #         'fields': ('publisher', 'developer')
    #     }),
    #     ('Game content', {
    #         'fields': ('screenshots', )
    #     })),

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
    """Game tag admin model"""
    list_display = ('name', 'slug', )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Game genre admin model"""
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
    """Game discount admin model"""
    pass


@admin.register(ItemPlatform)
class ItemPlatformAdmin(admin.ModelAdmin):
    """Game platform admin model"""
    list_display = ('name', 'slug')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """Game language admin model"""
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    """Game region of activation admin model"""
    pass
