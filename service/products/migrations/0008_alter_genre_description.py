# Generated by Django 3.2 on 2023-02-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20230216_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]