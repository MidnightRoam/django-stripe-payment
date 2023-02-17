# Generated by Django 3.2 on 2023-02-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('USD', 'Usd'), ('Euro', 'Euro')], default='USD', max_length=20),
        ),
    ]