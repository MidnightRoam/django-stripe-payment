from django.forms import ModelForm

from .models import ItemRating


class ItemRatingForm(ModelForm):
    class Meta:
        model = ItemRating
        fields = ('rate', 'text')
