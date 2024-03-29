# Generated by Django 3.2.4 on 2023-04-06 10:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0097_auto_20230406_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='parent_game',
        ),
        migrations.AddField(
            model_name='item',
            name='parent_game',
            field=models.ManyToManyField(blank=True, null=True, related_name='_products_item_parent_game_+', to='products.Item', verbose_name="Parent game (if it's a DLC)"),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('Game', 'Original game'), ('DLC', 'DLC')], default='Game', max_length=15),
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 6, 10, 21, 0, 969620, tzinfo=utc)),
        ),
    ]
