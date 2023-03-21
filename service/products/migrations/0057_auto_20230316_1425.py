# Generated by Django 3.2.4 on 2023-03-16 13:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0056_alter_itemdiscount_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='poster',
            field=models.ImageField(blank=True, upload_to='products/product_posters'),
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 16, 13, 25, 42, 41295, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemscreenshot',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/product_screenshots', verbose_name='Screenshot'),
        ),
    ]