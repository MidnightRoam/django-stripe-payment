# Generated by Django 3.2.4 on 2023-02-23 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_rename_infavorites_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemScreenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='static/vendor/product_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.item')),
            ],
        ),
    ]
