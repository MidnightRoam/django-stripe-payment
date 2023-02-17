from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Item(models.Model):
    """Product item model"""

    class ItemCurrency(models.TextChoices):
        """Product currency choices"""
        USD = '$',
        Euro = '€',

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)  # in cents
    currency = models.CharField(max_length=20, choices=ItemCurrency.choices, default=ItemCurrency.USD)
    tags = models.ManyToManyField('Tag')
    poster = models.ImageField(upload_to='static/vendor/product_images', blank=True)

    def __str__(self):
        return self.name

    def get_price(self):
        """Return converted price from cents to dollars"""
        return "{0:.2f}".format(self.price / 100)

    def get_tags(self):
        """Return formatted string with all item tags"""
        return ", ".join([tag.name for tag in self.tags.all()])

    def get_absolute_url(self):
        """Return absolute url for each item"""
        return reverse('item_detail', kwargs={'pk': self.pk})


class Tag(models.Model):
    """Item genre model"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute url for each item tag"""
        return reverse('items_sort', kwargs={'pk': self.pk})


class Customer(models.Model):
    """Customer model"""
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=True, blank=True,)
    email = models.EmailField(max_length=100, null=True, blank=True,)
    device = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.device


class Order(models.Model):
    """Order items model"""
    item = models.ManyToManyField(Item)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, default='')

