from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _

from products.models import Item


class ItemRating(models.Model):
    """Product rating model"""
    class ItemRatingChoices(models.TextChoices):
        One = '1', _('1')
        Two = '2', _('2')
        Three = '3', _('3')
        Four = '4', _('4')
        Five = '5', _('5')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    rate = models.CharField(choices=ItemRatingChoices.choices, max_length=10)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            UniqueConstraint(fields=('user', 'item'), name='product_user_unique'),
        ]
        ordering = ['-created_at']
