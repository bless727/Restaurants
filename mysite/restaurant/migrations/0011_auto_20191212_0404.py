# Generated by Django 2.2 on 2019-12-12 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_auto_20191212_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recipeOfOwner', to='restaurant.User'),
        ),
    ]
