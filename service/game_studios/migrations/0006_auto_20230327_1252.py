# Generated by Django 3.2.4 on 2023-03-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_studios', '0005_auto_20230324_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='image',
            field=models.ImageField(blank=True, height_field=500, upload_to='game_studios/developers_images', width_field=500),
        ),
        migrations.AddField(
            model_name='publisher',
            name='image',
            field=models.ImageField(blank=True, height_field=500, upload_to='game_studios/publishers_images', width_field=500),
        ),
    ]
