# Generated by Django 3.2.4 on 2023-03-10 11:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_auto_20230310_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemplatform',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='platform',
            field=models.ManyToManyField(to='products.ItemPlatform'),
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 10, 11, 8, 55, 517353, tzinfo=utc)),
        ),
    ]