# Generated by Django 3.2.4 on 2023-03-23 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0073_auto_20230323_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 13, 42, 1, 510915, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='minimalsystemrequirements',
            name='processor',
            field=models.CharField(default='Intel', max_length=60, verbose_name='Processor'),
        ),
    ]
