# Generated by Django 3.2.4 on 2023-02-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20230223_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemrating',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
