# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-10 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1260', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1260ideadquir',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')]),
        ),
    ]
