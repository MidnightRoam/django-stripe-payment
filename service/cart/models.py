from django.db import models

from products.models import Customer, Item


class Order(models.Model):
    """Order items model"""
    item = models.ManyToManyField(Item)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, default='')
