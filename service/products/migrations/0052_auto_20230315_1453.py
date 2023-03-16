# Generated by Django 3.2.4 on 2023-03-15 13:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0051_alter_itemdiscount_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='products.Tag', verbose_name='Genres / tags'),
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 15, 13, 53, 25, 449877, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemplatform',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='itemscreenshot',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_images', verbose_name='Screenshot'),
        ),
    ]
