# Generated by Django 5.0.6 on 2024-07-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_delete_casocliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_cliente', models.CharField(max_length=12)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('telefono_cliente', models.CharField(max_length=20)),
                ('email_cliente', models.EmailField(max_length=254)),
                ('descripcion_caso', models.TextField()),
                ('estado', models.CharField(default='En proceso', max_length=20)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
