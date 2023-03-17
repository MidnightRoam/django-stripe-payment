from django.contrib import admin

from .models import ItemRating


@admin.register(ItemRating)
class ItemRatingAdmin(admin.ModelAdmin):
    """Favorite admin model"""
    pass
