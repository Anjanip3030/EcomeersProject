# Generated by Django 3.0 on 2021-04-16 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('mi', 'mi'), ('oppo', 'oppo'), ('vivo', 'vivo'), ('apple', 'apple')], max_length=100),
        ),
    ]
