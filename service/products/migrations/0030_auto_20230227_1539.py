# Generated by Django 3.2.4 on 2023-02-27 14:39

from django.db import migrations, models
import django.utils.timezone
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_auto_20230224_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='item',
            name='modified',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('Common', 'Common'), ('New', 'New'), ('Outdated', 'Outdated')], default='New', max_length=20),
        ),
        migrations.DeleteModel(
            name='ItemReviewLike',
        ),
    ]
