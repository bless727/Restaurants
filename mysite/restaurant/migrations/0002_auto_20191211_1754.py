# Generated by Django 2.2 on 2019-12-11 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='step_text',
            field=models.TextField(max_length=200),
        ),
    ]
