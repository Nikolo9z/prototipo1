# Generated by Django 2.0.2 on 2022-04-03 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piso', models.CharField(max_length=1)),
                ('tipo1', models.CharField(choices=[('Vip', 'Vip'), ('C', 'Colaborador'), ('V', 'Visita')], max_length=3)),
                ('tipo2', models.CharField(choices=[('A', 'Auto'), ('B', 'Bus'), ('M', 'Moto'), ('C', 'Bicicleta')], max_length=3)),
                ('telefono', models.CharField(max_length=9)),
            ],
        ),
    ]
