# Generated by Django 3.2.4 on 2023-03-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(editable=False, max_length=200),
        ),
    ]