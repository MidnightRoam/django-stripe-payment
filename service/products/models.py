from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    """Product item model"""

    class ItemCurrency(models.TextChoices):
        USD = 'USD',
        Euro = 'Euro',

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)  # in cents
    currency = models.CharField(max_length=20, choices=ItemCurrency.choices, default=ItemCurrency.USD)

    def __str__(self):
        return self.name

    def get_price(self):
        return "{0:.2f}".format(self.price / 100)

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'pk': self.pk})


class Order(models.Model):
    """Order items model"""
    item = models.ManyToManyField(Item)
