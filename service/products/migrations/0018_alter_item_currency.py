# Generated by Django 3.2 on 2023-02-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('$', 'Usd'), ('€', 'Euro')], default='$', max_length=20),
        ),
    ]