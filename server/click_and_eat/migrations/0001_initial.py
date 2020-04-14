# Generated by Django 3.0.5 on 2020-04-14 12:08

import click_and_eat.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('logo', models.ImageField(upload_to=click_and_eat.models.restaurant_data_directory_path)),
                ('preview_image', models.ImageField(upload_to=click_and_eat.models.restaurant_data_directory_path)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('photo', models.ImageField(null=True, upload_to=click_and_eat.models.restaurant_products_directory_path)),
                ('price', models.PositiveIntegerField()),
                ('value', models.CharField(max_length=16)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='click_and_eat.Category')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='click_and_eat.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='click_and_eat.Restaurant'),
        ),
        migrations.CreateModel(
            name='AddressOfRestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='click_and_eat.Restaurant')),
            ],
        ),
    ]
