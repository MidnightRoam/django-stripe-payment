# Generated by Django 3.2 on 2023-02-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230213_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('usd', 'Usd'), ('euro', 'Euro')], default='usd', max_length=20),
        ),
    ]