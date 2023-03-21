from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .translate import from_cyrillic_to_latin


class Item(models.Model):
    """Product item model"""
    class ItemCurrency(models.TextChoices):
        """Product currency choices"""
        USD = '$',
        Euro = '€',

    class ItemStatus(models.TextChoices):
        """Product status choices"""
        common = 'Common',
        new = 'New',
        outdated = 'Outdated',

    name = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField()
    price = models.IntegerField(default=0)  # in cents
    currency = models.CharField(max_length=20, choices=ItemCurrency.choices, default=ItemCurrency.USD)
    tags = models.ManyToManyField('Tag', verbose_name='Genres / tags')
    platform = models.ManyToManyField('ItemPlatform')
    poster = models.ImageField(upload_to='products/product_posters', blank=True)
    trailer = models.URLField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=ItemStatus.choices, default=ItemStatus.new)
    created = models.DateTimeField(editable=False, blank=True, default=timezone.now)
    modified = models.DateTimeField(blank=True, default=timezone.now)
    slug = models.SlugField(max_length=100, editable=False, default='')

    def save(self, *args, **kwargs):
        """Auto set slug field as item name"""
        if not self.slug:
            self.slug = from_cyrillic_to_latin(str(self.name))
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_price(self):
        """Return converted price from cents to dollars"""
        return self.currency + "{0:.2f}".format(self.price / 100)

    def get_discounted_price(self):
        """Return converted price from cents to dollars including discount"""
        discount = self.discounts.filter(end_date__gte=timezone.now()).last()
        if discount:
            discount = self.price * float(discount.value)
            price = (self.price - discount) / 100
        else:
            price = self.price / 100
        return self.currency + "{0:.2f}".format(price)

    def get_price_stripe(self):
        """Return price for stripe payment"""
        discount = self.discounts.filter(end_date__gte=timezone.now()).last()
        if discount:
            discount = float(discount.value)
            round_price = round((self.price - self.price * discount) / 100, 2)
            price_in_cents = round(round_price * 100)
        else:
            price_in_cents = self.price
        return price_in_cents

    def get_percent_discount(self):
        """Return percent discount"""
        discount = self.discounts.filter(end_date__gte=timezone.now()).last()
        if discount:
            return "{:.0%}".format(float(discount.value))

    def get_tags(self):
        """Return formatted string with all item tags"""
        return ", ".join([tag.name for tag in self.tags.all()])

    def get_absolute_url(self):
        """Return absolute url for each item"""
        return reverse('item_detail', kwargs={'pk': self.pk})

    def get_short_description(self):
        """Return short description for product card"""
        short_description = self.description[:220]
        if short_description.endswith('.'):
            return short_description + '..'
        else:
            return short_description + '...'


class ItemScreenshot(models.Model):
    """Item screenshots model"""
    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='products/product_screenshots', blank=True, verbose_name='Screenshot')


class ItemDiscount(models.Model):
    """Item discount model"""
    class DiscountValue(models.TextChoices):
        """Discount value choices"""
        ten_percent = 0.10, '10%'
        twenty_percent = 0.20, '20%'
        thirty_percent = 0.30, '30%'
        fifty_percent = 0.50, '50%'
        eighty_percent = 0.80, '80%'

    class DiscountEndDates(models.TextChoices):
        """Discount end date choices"""
        test = timezone.timedelta(days=1), '1 day'
        days_7 = timezone.timedelta(days=7), '7 days'
        days_14 = timezone.timedelta(days=14), '14 days'

    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='discounts')
    value = models.CharField(max_length=20, choices=DiscountValue.choices)
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.CharField(max_length=30, choices=DiscountEndDates.choices, default=DiscountEndDates.days_7)
    name = models.CharField(max_length=50, blank=True)


class ItemPlatform(models.Model):
    """Product platform (PC/PS4/PS5/XBOX etc) model"""
    class ItemPlatformChoice(models.TextChoices):
        """Product platform choices"""
        steam = 'Steam',
        xbox = 'Xbox',
        rockstar_games = 'Rockstar Games',
        uplay = 'Uplay',
        epic_games = 'Epic Games',

    name = models.CharField(max_length=100, choices=ItemPlatformChoice.choices, blank=True)
    icon = models.FileField(blank=True, null=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'svg'])])
    slug = models.SlugField(max_length=100, blank=True, editable=False)

    def save(self, *args, **kwargs):
        """Auto set slug field as item platform name"""
        if not self.slug:
            self.slug = from_cyrillic_to_latin(str(self.name))
        super(ItemPlatform, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute url for each item platform"""
        return reverse('index', kwargs={'platform_slug': self.slug})


class Tag(models.Model):
    """Item genre model"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, default='', editable=False)

    def save(self, *args, **kwargs):
        """Auto set slug field as item name"""
        if not self.slug:
            self.slug = from_cyrillic_to_latin(str(self.name))
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute url for each item tag"""
        return reverse('index', kwargs={'tag_slug': self.slug})


class ItemDLC(models.Model):
    """Product DLC model"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)  # in cents
    product = models.ForeignKey(Item, verbose_name='Game', blank=True, on_delete=models.CASCADE)


class Customer(models.Model):
    """Customer model"""
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=True, blank=True,)
    email = models.EmailField(max_length=100, null=True, blank=True,)
    device = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.device


class Favorite(models.Model):
    """Favorites items model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

