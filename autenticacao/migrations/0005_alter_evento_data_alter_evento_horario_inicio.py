# Generated by Django 5.1.5 on 2025-02-11 14:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0004_alter_evento_data_alter_evento_horario_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horario_inicio',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
