# Generated by Django 3.2.4 on 2023-03-23 13:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0069_auto_20230323_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinimalSystemRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oc', models.CharField(default='Windows 10', max_length=50, verbose_name='OS')),
                ('processor', models.CharField(default='Intel', max_length=150, verbose_name='Processor')),
                ('graphics_card', models.CharField(default='Windows 10', max_length=150, verbose_name='Graphics card')),
                ('ram', models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (4, 'Four'), (6, 'Six'), (8, 'Eight'), (16, 'Sixteen')], default=4, max_length=150, verbose_name='RAM')),
                ('directx', models.CharField(choices=[('Version 12', 'Version 12'), ('Version 11', 'Version 11'), ('Version 10', 'Version 10'), ('Version 9', 'Version 9'), ('Version 8', 'Version 8')], default='Version 11', max_length=50, verbose_name='DirectX')),
                ('disk_space', models.PositiveSmallIntegerField(default='20', max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 13, 0, 43, 266990, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemlocalization',
            name='game',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='products.item'),
        ),
        migrations.AlterField(
            model_name='itemlocalization',
            name='language',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.language', verbose_name='Language'),
        ),
    ]
