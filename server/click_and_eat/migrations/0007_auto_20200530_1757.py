# Generated by Django 3.0.3 on 2020-05-30 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('click_and_eat', '0006_auto_20200524_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='categories',
            field=models.ManyToManyField(related_name='provider', to='click_and_eat.RestaurantCategory'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='main_category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='click_and_eat.RestaurantCategory'),
        ),
    ]