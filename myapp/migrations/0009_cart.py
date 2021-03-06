# Generated by Django 3.0 on 2021-04-17 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210416_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User')),
            ],
        ),
    ]
