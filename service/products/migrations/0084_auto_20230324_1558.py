# Generated by Django 3.2.4 on 2023-03-24 14:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game_studios', '0005_auto_20230324_1541'),
        ('products', '0083_auto_20230324_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='publisher',
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 24, 14, 58, 35, 711176, tzinfo=utc)),
        ),
    ]
