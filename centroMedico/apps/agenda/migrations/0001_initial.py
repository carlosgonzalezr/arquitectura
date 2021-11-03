# Generated by Django 3.2.6 on 2021-10-30 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('id_agenda', models.IntegerField(max_length=11)),
                ('fecha_pago', models.DateField()),
                ('monto_pago', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('id_region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=14)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('id_comuna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_especialidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.especialidad')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.persona')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='id_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.region'),
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.medico')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.sucursal')),
            ],
        ),
    ]