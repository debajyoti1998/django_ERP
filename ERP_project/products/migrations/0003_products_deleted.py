# Generated by Django 3.1.4 on 2020-12-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='deleted',
            field=models.IntegerField(default=0, max_length=2),
        ),
    ]