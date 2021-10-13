# Generated by Django 3.2.7 on 2021-10-12 23:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HVApp', '0003_rename_profecion_hojadevida_profesion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hojadevida',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='hojadevida',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='hojadevida',
            name='nombre',
        ),
        migrations.AddField(
            model_name='hojadevida',
            name='user',
            field=models.ForeignKey(default= 1, on_delete=django.db.models.deletion.CASCADE, related_name='HojaDeVida', to='HVApp.user'),
            preserve_default=False,
        ),
    ]