# Generated by Django 3.2.7 on 2021-10-06 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HVApp', '0002_hojadevida'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hojadevida',
            old_name='profecion',
            new_name='profesion',
        ),
    ]
