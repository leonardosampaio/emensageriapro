# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-20 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('r2050', '0002_auto_20181118_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2050infoproc',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r2050infoproc',
            name='nrproc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='r2050infoproc',
            name='r2050_tipocom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r2050infoproc_r2050_tipocom', to='r2050.r2050tipoCom'),
        ),
        migrations.AlterField(
            model_name='r2050infoproc',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')]),
        ),
        migrations.AlterField(
            model_name='r2050tipocom',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r2050tipocom',
            name='indcom',
            field=models.IntegerField(choices=[(1, '1 - Comercializa\xe7\xe3o da Produ\xe7\xe3o por Prod. Rural PJ/Agroind\xfastria, exceto para entidades executoras do PAA'), (8, '8 - Comercializa\xe7\xe3o da Produ\xe7\xe3o para Entidade do Programa de Aquisi\xe7\xe3o de Alimentos - PAA'), (9, '9 - Comercializa\xe7\xe3o direta da Produ\xe7\xe3o no Mercado Externo')]),
        ),
        migrations.AlterField(
            model_name='r2050tipocom',
            name='r2050_evtcomprod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r2050tipocom_r2050_evtcomprod', to='efdreinf.r2050evtComProd'),
        ),
        migrations.AlterField(
            model_name='r2050tipocom',
            name='vlrrecbruta',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
    ]