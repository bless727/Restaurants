# Generated by Django 2.2 on 2019-12-11 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20191211_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
