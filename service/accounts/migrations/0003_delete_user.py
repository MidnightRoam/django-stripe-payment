# Generated by Django 3.2 on 2023-02-21 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230221_1318'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
