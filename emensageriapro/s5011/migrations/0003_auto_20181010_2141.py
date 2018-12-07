# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-10 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s5011', '0002_auto_20180912_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s5011dadosopport',
            name='aliqrat',
            field=models.IntegerField(choices=[(1, '1 - 1'), (2, '2 - 2'), (3, '3 - 3')]),
        ),
        migrations.AlterField(
            model_name='s5011ideestab',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')]),
        ),
        migrations.AlterField(
            model_name='s5011infoestab',
            name='aliqrat',
            field=models.IntegerField(choices=[(1, '1 - 1'), (2, '2 - 2'), (3, '3 - 3')]),
        ),
    ]
