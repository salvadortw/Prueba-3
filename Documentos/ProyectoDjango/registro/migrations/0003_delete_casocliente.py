# Generated by Django 5.0.6 on 2024-07-01 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_rename_fecha_casocliente_fecha_registro_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CasoCliente',
        ),
    ]
