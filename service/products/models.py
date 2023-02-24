from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
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


class ItemScreenshot(models.Model):
    """Item screenshots model"""
    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='product_images', blank=True)


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


class Favorite(models.Model):
    """Favorites items model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


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
