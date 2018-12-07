# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-20 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2231', '0002_auto_20181119_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2231fimcessao',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2231fimcessao',
            name='dttermcessao',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s2231fimcessao',
            name='s2231_evtcessao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2231fimcessao_s2231_evtcessao', to='esocial.s2231evtCessao'),
        ),
        migrations.AlterField(
            model_name='s2231inicessao',
            name='cnpjcess',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='s2231inicessao',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2231inicessao',
            name='dtinicessao',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s2231inicessao',
            name='indcessao',
            field=models.IntegerField(choices=[(1, '1 - Cess\xe3o'), (2, '2 - Agente p\xfablico \xe0 disposi\xe7\xe3o da Justi\xe7a Eleitoral'), (3, '3 - Exerc\xedcio em outro \xf3rg\xe3o, em caso diferente de cess\xe3o')]),
        ),
        migrations.AlterField(
            model_name='s2231inicessao',
            name='infonus',
            field=models.IntegerField(choices=[(1, '1 - Pagamento exclusivamente pelo cedente/origem'), (2, '2 - Pagamento exclusivamente pelo cession\xe1rio/destino'), (3, '3 - Pagamento pelo cedente/origem e pelo cession\xe1rio/destino'), (4, '4 - Pagamento pelo cedente/origem com ressarcimento pelo cession\xe1rio/destino')]),
        ),
        migrations.AlterField(
            model_name='s2231inicessao',
            name='s2231_evtcessao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2231inicessao_s2231_evtcessao', to='esocial.s2231evtCessao'),
        ),
    ]
