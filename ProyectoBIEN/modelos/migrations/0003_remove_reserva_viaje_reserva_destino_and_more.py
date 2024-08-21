# Generated by Django 5.0.6 on 2024-08-21 01:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0002_tours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='viaje',
        ),
        migrations.AddField(
            model_name='reserva',
            name='destino',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='modelos.tours', verbose_name='Destino'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario '),
        ),
    ]
