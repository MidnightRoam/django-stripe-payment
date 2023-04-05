from django.core.validators import FileExtensionValidator
from django.db.models.fields import related
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .translate import from_cyrillic_to_latin

from game_studios.models import Publisher, Developer


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

    class ItemType(models.TextChoices):
        """Game type choices"""
        game = 'Game',
        addon = 'DLC'

    name = models.CharField(max_length=100, verbose_name='Title')
    tagline = models.CharField(max_length=150, verbose_name='Tagline', default='Game is waiting!')
    description = models.TextField()
    price = models.IntegerField(default=0)  # in cents
    currency = models.CharField(max_length=20, choices=ItemCurrency.choices, default=ItemCurrency.USD)
    tags = models.ManyToManyField('Tag', verbose_name='Game tags')
    genre = models.ManyToManyField('Genre', verbose_name='Game genres')
    platform = models.ManyToManyField('ItemPlatform')
    publisher = models.ManyToManyField(Publisher)
    developer = models.ManyToManyField(Developer)
    poster = models.ImageField(upload_to='products/product_posters', blank=True)
    status = models.CharField(max_length=20, choices=ItemStatus.choices, default=ItemStatus.new)
    created = models.DateTimeField(editable=False, blank=True, default=timezone.now)
    modified = models.DateTimeField(blank=True, default=timezone.now)
    slug = models.SlugField(max_length=100, editable=False, default='')
    amount = models.IntegerField(default=0)
    type = models.CharField(max_length=15, choices=ItemType.choices, default=ItemType.game)

    def save(self, *args, **kwargs):
        """Auto set slug field as item name"""
        bad_symbols = ['.', ',', ':', '!', '@', '?']
        result_slug = ''
        if not self.slug:
            for i in self.name:
                if i not in bad_symbols:
                    result_slug += i
            self.slug = from_cyrillic_to_latin(str(result_slug))
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

    def get_genres(self):
        """Return formatted string with all game genres"""
        return ", ".join([genre.name for genre in self.genre.all()])

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

    def get_tagline(self):
        """Return tagline in uppercase"""
        tagline = str(self.tagline)
        return tagline.upper()

    def get_platforms(self):
        """Return string with all game platforms"""
        lst = self.platform.name
        return lst

    def get_product_in_stock(self):
        """
        Return string
        'In stock' - if amount of product > 1
        of
        'SOLD OUT' - if amount of product < 1
        """
        result = 'In stock'
        if self.amount < 1:
            result = 'SOLD OUT'
        return result


class Addon(Item):
    """Game DLC model"""
    game = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='addons')


class ItemScreenshot(models.Model):
    """Game screenshots model"""
    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='products/product_screenshots', blank=True, verbose_name='Screenshot')


class GameTrailer(models.Model):
    """Game trailers model"""
    url = models.URLField(blank=True)
    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='trailers')

    def save(self, *args, **kwargs):
        """Auto set url field for game trailer"""
        # if not self.pk and not self.url:
        url = str(self.url)
        replacer = 'https://youtu.be/'
        if replacer in url:
            url = url.replace(replacer, '')
            result_url = f'https://www.youtube.com/embed/{url}'
            self.url = result_url
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


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
        """Auto set slug field as tag name"""
        if not self.slug:
            self.slug = from_cyrillic_to_latin(str(self.name))
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute url for each item tag"""
        return reverse('index', kwargs={'tag_slug': self.slug})


class Genre(models.Model):
    """Game genre model"""
    name = models.CharField(max_length=124)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=124, default='', editable=False)

    def save(self, *args, **kwargs):
        """Auto set slug field as genre name"""
        if not self.slug:
            slug = str(self.name).replace(' ', '_').lower()
            self.slug = slug
        super(Genre, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for each game genre"""
        return reverse('index', kwargs={'genre_slug': self.slug})

    def __str__(self):
        return self.name


class ItemDLC(models.Model):
    """Product DLC model"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)  # in cents
    product = models.ForeignKey(Item, verbose_name='Game', blank=True, on_delete=models.CASCADE)


class Language(models.Model):
    """Language model"""
    class LanguageChoice(models.TextChoices):
        """name field choices"""
        english = 'English'
        russian = 'Russian'
        german = 'German'
        spanish = 'Spanish'
        french = 'French'
        italian = 'Italian'
        japanese = 'Japanese'
        korean = 'Korean'
        chinese = 'Chinese'

    name = models.CharField(choices=LanguageChoice.choices, default=LanguageChoice.english, max_length=100)

    def __str__(self):
        return self.name


class ItemLocalization(models.Model):
    """Product localization model"""
    language = models.ForeignKey(Language, verbose_name='Language', blank=True, on_delete=models.CASCADE)
    interface = models.BooleanField(default=0, verbose_name='Interface')
    subtitles = models.BooleanField(default=0, verbose_name='Subtitles')
    voice_acting = models.BooleanField(default=0, verbose_name='Voice acting')
    game = models.ForeignKey('Item', on_delete=models.CASCADE, default=0, related_name='languages')

    def __str__(self):
        return self.language.name

    def get_language_option(self):
        """
        Returns formatted string with language and option
        (subtitles or voice acting or only interface localizated)
        """
        options = []
        if self.interface:
            options.append('interface')
        if self.subtitles:
            options.append('subtitles')
        if self.voice_acting:
            options.append('voice')
        result_options = ', '.join(options)
        return f'{result_options}'


class MinimalSystemRequirements(models.Model):
    """Minimal game system requirements model"""
    class RamChoices(models.IntegerChoices):
        """memory (ram) field choices"""
        one = 1, _('1')
        two = 2, _('2')
        four = 4, _('4')
        six = 6, _('6')
        eight = 8, _('8')
        twelve = 12, _('12')
        sixteen = 16, _('16')

    class DirectxChoices(models.TextChoices):
        """directx field choices"""
        version_12 = 'Version 12',
        version_11 = 'Version 11'
        version_10 = 'Version 10'
        version_9 = 'Version 9'
        version_8 = 'Version 8'

    os = models.CharField(max_length=50, default='Windows 10', verbose_name='OS')
    processor = models.CharField(max_length=60, default='Intel', verbose_name='Processor')
    graphics_card = models.CharField(max_length=150, default='NVIDIA or AMD', verbose_name='Graphics card')
    ram = models.IntegerField(max_length=150, choices=RamChoices.choices, default=RamChoices.four, verbose_name='RAM')
    directx = models.CharField(max_length=50,
                               choices=DirectxChoices.choices,
                               default=DirectxChoices.version_11,
                               verbose_name='DirectX'
                               )
    disk_space = models.PositiveSmallIntegerField(max_length=3, default='20')
    game = models.ForeignKey(Item, on_delete=models.CASCADE, default=0, related_name='minimal_system_requirements')

    def save(self, *args, **kwargs):
        """Replace some symbols in text if they exist"""
        replace_symbols = ['®', '™']
        processor = self.processor
        graphics_card = self.graphics_card
        for symbol in processor:
            if symbol in replace_symbols:
                self.processor = processor.replace(symbol, '')
        for symbol in graphics_card:
            if symbol in replace_symbols:
                self.graphics_card = graphics_card.replace(symbol, '')
        super(MinimalSystemRequirements, self).save(*args, **kwargs)


class Region(models.Model):
    """All regions model"""
    name = models.CharField(max_length=124)

    def __str__(self):
        return self.name


class RegionOfActivation(models.Model):
    """Game region of activation model"""
    region = models.ForeignKey(Region, default='0', on_delete=models.CASCADE)
    game = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='regions')


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

