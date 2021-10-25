# Generated by Django 3.2.6 on 2021-10-25 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=50)),
                ('medico', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pageprincipal.especialidad')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pageprincipal.sucursal')),
            ],
        ),
    ]
