# Generated by Django 3.2.4 on 2023-03-10 13:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0045_auto_20230310_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemplatform',
            name='slug',
            field=models.SlugField(default='<built-in function id>', max_length=100),
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 10, 13, 45, 29, 757026, tzinfo=utc)),
        ),
    ]
