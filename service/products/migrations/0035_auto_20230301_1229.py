# Generated by Django 3.2.4 on 2023-03-01 11:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20230301_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdiscount',
            name='end_date',
            field=models.CharField(choices=[('1 day, 0:00:00', '1 day'), ('7 days, 0:00:00', '7 days'), ('14 days, 0:00:00', '14 days')], default='7 days, 0:00:00', max_length=30),
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 11, 29, 1, 937609, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='value',
            field=models.CharField(choices=[('0.1', '10%'), ('0.2', '20%'), ('0.3', '30%'), ('0.5', '50%'), ('0.8', '80%')], max_length=20),
        ),
    ]
