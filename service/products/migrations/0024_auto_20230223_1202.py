# Generated by Django 3.2.4 on 2023-02-23 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0023_itemscreenshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemscreenshot',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='itemscreenshot',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenshots', to='products.item'),
        ),
        migrations.CreateModel(
            name='ItemRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], max_length=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]