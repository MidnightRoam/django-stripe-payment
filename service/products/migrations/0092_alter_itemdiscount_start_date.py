# Generated by Django 3.2.4 on 2023-04-03 15:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0091_auto_20230403_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 3, 15, 48, 32, 556365, tzinfo=utc)),
        ),
    ]