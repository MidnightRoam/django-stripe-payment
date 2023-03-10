# Generated by Django 3.2.4 on 2023-03-10 12:39

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0042_auto_20230310_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 10, 12, 39, 54, 216305, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemplatform',
            name='icon',
            field=models.FileField(blank=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'svg'])]),
        ),
    ]
