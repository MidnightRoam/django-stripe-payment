# Generated by Django 3.2.4 on 2023-02-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20230223_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemrating',
            name='rate',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10),
        ),
        migrations.AddConstraint(
            model_name='itemrating',
            constraint=models.UniqueConstraint(fields=('user', 'item'), name='product_user_unique'),
        ),
    ]
