# Generated by Django 3.2 on 2023-02-16 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='poster',
        ),
    ]
