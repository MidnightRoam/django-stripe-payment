from django.db import models


class Item(models.Model):
    """Product item model"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)  # in cents

    def __str__(self):
        return self.name

    def get_price(self):
        return "{0:.2f}".format(self.price / 100)


class Order(models.Model):
    """Order items model"""
    item = models.OneToManyField("Item")