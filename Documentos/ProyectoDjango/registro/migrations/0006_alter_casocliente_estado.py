# Generated by Django 5.0.6 on 2024-07-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_remove_casocliente_email_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casocliente',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En proceso'), ('resuelto', 'Resuelto')], default='pendiente', max_length=20),
        ),
    ]
