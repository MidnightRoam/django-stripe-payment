# Generated by Django 3.2 on 2023-02-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_item_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('USD', 'Usd'), ('Euro', 'Euro')], default='USD', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='genres',
            field=models.ManyToManyField(to='products.Genre'),
        ),
    ]