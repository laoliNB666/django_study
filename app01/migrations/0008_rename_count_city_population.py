# Generated by Django 3.2 on 2022-09-17 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_boss_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='count',
            new_name='population',
        ),
    ]
