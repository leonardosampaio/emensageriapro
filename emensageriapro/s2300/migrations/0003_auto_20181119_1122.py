# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-19 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0008_auto_20181118_2229'),
        ('esocial', '0005_auto_20181119_0958'),
        ('s2300', '0002_auto_20180912_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='s2300mudancaCPF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpfant', models.CharField(default=b'A', max_length=11)),
                ('dtaltcpf', models.DateField(default=b'1900-01-01')),
                ('observacao', models.CharField(blank=True, max_length=255, null=True)),
                ('criado_em', models.DateTimeField()),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2300mudancacpf_criado_por', to='controle_de_acesso.Usuarios')),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2300mudancacpf_modificado_por', to='controle_de_acesso.Usuarios')),
                ('s2300_evttsvinicio', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300mudancacpf_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio')),
            ],
            options={
                'ordering': ['s2300_evttsvinicio', 'cpfant', 'dtaltcpf'],
                'db_table': 's2300_mudancacpf',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='s2300documentos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2300documentos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2300documentos',
            name='s2300_evttsvinicio',
        ),
        migrations.RemoveField(
            model_name='s2300infocomplementares',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2300infocomplementares',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2300infocomplementares',
            name='s2300_evttsvinicio',
        ),
        migrations.AlterModelOptions(
            name='s2300ageintegracao',
            options={'managed': True, 'ordering': ['s2300_infoestagiario', 'cnpjagntinteg', 'nmrazao', 'dsclograd', 'nrlograd', 'cep', 'uf']},
        ),
        migrations.AlterModelOptions(
            name='s2300brasil',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'tplograd', 'dsclograd', 'nrlograd', 'cep', 'codmunic', 'uf']},
        ),
        migrations.AlterModelOptions(
            name='s2300cargofuncao',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'codcargo']},
        ),
        migrations.AlterModelOptions(
            name='s2300cnh',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'nrregcnh', 'ufcnh', 'dtvalid', 'categoriacnh']},
        ),
        migrations.AlterModelOptions(
            name='s2300contato',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio']},
        ),
        migrations.AlterModelOptions(
            name='s2300ctps',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'nrctps', 'seriectps', 'ufctps']},
        ),
        migrations.AlterModelOptions(
            name='s2300dependente',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'tpdep', 'nmdep', 'dtnascto', 'depirrf', 'depsf', 'inctrab']},
        ),
        migrations.AlterModelOptions(
            name='s2300exterior',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'paisresid', 'dsclograd', 'nrlograd', 'nmcid']},
        ),
        migrations.AlterModelOptions(
            name='s2300fgts',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'opcfgts']},
        ),
        migrations.AlterModelOptions(
            name='s2300infodeficiencia',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'deffisica', 'defvisual', 'defauditiva', 'defmental', 'defintelectual', 'reabreadap']},
        ),
        migrations.AlterModelOptions(
            name='s2300infodirigentesindical',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'categorig']},
        ),
        migrations.AlterModelOptions(
            name='s2300infoestagiario',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'natestagio', 'nivestagio', 'dtprevterm', 'nmrazao']},
        ),
        migrations.AlterModelOptions(
            name='s2300infotrabcedido',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'categorig', 'cnpjcednt', 'matricced', 'dtadmced', 'tpregtrab', 'tpregprev', 'infonus']},
        ),
        migrations.AlterModelOptions(
            name='s2300oc',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'nroc', 'orgaoemissor']},
        ),
        migrations.AlterModelOptions(
            name='s2300remuneracao',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'vrsalfx', 'undsalfixo']},
        ),
        migrations.AlterModelOptions(
            name='s2300rg',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'nrrg', 'orgaoemissor']},
        ),
        migrations.AlterModelOptions(
            name='s2300ric',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'nrric', 'orgaoemissor']},
        ),
        migrations.AlterModelOptions(
            name='s2300rne',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'nrrne', 'orgaoemissor']},
        ),
        migrations.AlterModelOptions(
            name='s2300trabestrangeiro',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'classtrabestrang', 'casadobr', 'filhosbr']},
        ),
        migrations.RemoveField(
            model_name='s2300cargofuncao',
            name='s2300_infocomplementares',
        ),
        migrations.RemoveField(
            model_name='s2300cnh',
            name='s2300_documentos',
        ),
        migrations.RemoveField(
            model_name='s2300ctps',
            name='s2300_documentos',
        ),
        migrations.RemoveField(
            model_name='s2300fgts',
            name='s2300_infocomplementares',
        ),
        migrations.RemoveField(
            model_name='s2300infodirigentesindical',
            name='s2300_infocomplementares',
        ),
        migrations.RemoveField(
            model_name='s2300infoestagiario',
            name='s2300_infocomplementares',
        ),
        migrations.RemoveField(
            model_name='s2300infotrabcedido',
            name='s2300_infocomplementares',
        ),
        migrations.RemoveField(
            model_name='s2300oc',
            name='s2300_documentos',
        ),
        migrations.RemoveField(
            model_name='s2300remuneracao',
            name='s2300_infocomplementares',
        ),
        migrations.RemoveField(
            model_name='s2300rg',
            name='s2300_documentos',
        ),
        migrations.RemoveField(
            model_name='s2300ric',
            name='s2300_documentos',
        ),
        migrations.RemoveField(
            model_name='s2300rne',
            name='s2300_documentos',
        ),
        migrations.AddField(
            model_name='s2300cargofuncao',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300cargofuncao_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AddField(
            model_name='s2300cnh',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300cnh_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AddField(
            model_name='s2300ctps',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300ctps_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AddField(
            model_name='s2300fgts',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300fgts_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AddField(
            model_name='s2300infodirigentesindical',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300infodirigentesindical_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AddField(
            model_name='s2300infoestagiario',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300infoestagiario_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AddField(
            model_name='s2300infotrabcedido',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300infotrabcedido_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AddField(
            model_name='s2300oc',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300oc_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AddField(
            model_name='s2300remuneracao',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300remuneracao_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AddField(
            model_name='s2300rg',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300rg_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AddField(
            model_name='s2300ric',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300ric_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AddField(
            model_name='s2300rne',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300rne_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AlterField(
            model_name='s2300afastamento',
            name='codmotafast',
            field=models.CharField(choices=[(b'01', '01 - Acidente/Doen\xe7a do trabalho'), (b'03', '03 - Acidente/Doen\xe7a n\xe3o relacionada ao trabalho'), (b'05', '05 - Afastamento/licen\xe7a prevista em regime pr\xf3prio (estatuto), sem remunera\xe7\xe3o'), (b'06', '06 - Aposentadoria por invalidez'), (b'07', '07 - Acompanhamento - Licen\xe7a para acompanhamento de membro da fam\xedlia enfermo'), (b'08', '08 - Afastamento do empregado para participar de atividade do Conselho Curador do FGTS - art. 65, \xa76\xba, Dec. 99.684/90 (Regulamento do FGTS)'), (b'10', '10 - Afastamento/licen\xe7a prevista em regime pr\xf3prio (estatuto), com remunera\xe7\xe3o'), (b'11', '11 - C\xe1rcere'), (b'12', '12 - Cargo Eletivo - Candidato a cargo eletivo - Lei 7.664/1988. art. 25\xb0, par\xe1grafo \xfanico - Celetistas em geral'), (b'13', '13 - Cargo Eletivo - Candidato a cargo eletivo - Lei Complementar 64/1990. art. 1\xb0, inciso II, al\xednea 1 - Servidor p\xfablico, estatut\xe1rio ou n\xe3o, dos \xf3rg\xe3os ou entidades da Administra\xe7\xe3o Direta ou Indireta da Uni\xe3o, dos Estados, do Distrito Federal, dos Muni (...)'), (b'14', '14 - Cess\xe3o / Requisi\xe7\xe3o'), (b'15', '15 - Gozo de f\xe9rias ou recesso - Afastamento tempor\xe1rio para o gozo de f\xe9rias ou recesso'), (b'16', '16 - Licen\xe7a remunerada - Lei, liberalidade da empresa ou Acordo/Conven\xe7\xe3o Coletiva de Trabalho'), (b'17', '17 - Licen\xe7a Maternidade - 120 dias e suas prorroga\xe7\xf5es/antecipa\xe7\xf5es, inclusive para o c\xf4njuge sobrevivente'), (b'18', '18 - Licen\xe7a Maternidade - 121 dias a 180 dias, Lei 11.770/2008 (Empresa Cidad\xe3), inclusive para o c\xf4njuge sobrevivente'), (b'19', '19 - Licen\xe7a Maternidade - Afastamento tempor\xe1rio por motivo de aborto n\xe3o criminoso'), (b'20', '20 - Licen\xe7a Maternidade - Afastamento tempor\xe1rio por motivo de licen\xe7a-maternidade decorrente de ado\xe7\xe3o ou guarda judicial de crian\xe7a, inclusive para o c\xf4njuge sobrevivente'), (b'21', '21 - Licen\xe7a n\xe3o remunerada ou Sem Vencimento'), (b'22', '22 - Mandato Eleitoral - Afastamento tempor\xe1rio para o exerc\xedcio de mandato eleitoral, sem remunera\xe7\xe3o'), (b'23', '23 - Mandato Eleitoral - Afastamento tempor\xe1rio para o exerc\xedcio de mandato eleitoral, com remunera\xe7\xe3o'), (b'24', '24 - Mandato Sindical - Afastamento tempor\xe1rio para exerc\xedcio de mandato sindical'), (b'25', '25 - Mulher v\xedtima de viol\xeancia - Lei 11.340/2006 - art. 9\xba \xa72o, II - Lei Maria da Penha'), (b'26', '26 - Participa\xe7\xe3o de empregado no Conselho Nacional de Previd\xeancia Social-CNPS (art. 3\xba, Lei 8.213/1991)'), (b'27', '27 - Qualifica\xe7\xe3o - Afastamento por suspens\xe3o do contrato de acordo com o art 476-A da CLT'), (b'28', '28 - Representante Sindical - Afastamento pelo tempo que se fizer necess\xe1rio, quando, na qualidade de representante de entidade sindical, estiver participando de reuni\xe3o oficial de organismo internacional do qual o Brasil seja membro'), (b'29', '29 - Servi\xe7o Militar - Afastamento tempor\xe1rio para prestar servi\xe7o militar obrigat\xf3rio;'), (b'30', '30 - Suspens\xe3o disciplinar - CLT, art. 474'), (b'31', '31 - Servidor P\xfablico em Disponibilidade'), (b'33', '33 - Licen\xe7a Maternidade - de 180 dias, Lei 13.301/2016.'), (b'34', '34 - Inatividade do trabalhador avulso (portu\xe1rio ou n\xe3o portu\xe1rio) por per\xedodo superior a 90 dias')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s2300afastamento',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300afastamento',
            name='dtiniafast',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2300afastamento',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300afastamento_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='cep',
            field=models.CharField(default=b'A', max_length=8),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='cnpjagntinteg',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='dsclograd',
            field=models.CharField(default=b'A', max_length=100),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='nmrazao',
            field=models.CharField(default=b'A', max_length=100),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='nrlograd',
            field=models.CharField(default=b'A', max_length=10),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='s2300_infoestagiario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300ageintegracao_s2300_infoestagiario', to='s2300.s2300infoEstagiario'),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='uf',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='cep',
            field=models.CharField(default=b'A', max_length=8),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='codmunic',
            field=models.TextField(default=b'0', max_length=7),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='dsclograd',
            field=models.CharField(default=b'A', max_length=100),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='nrlograd',
            field=models.CharField(default=b'A', max_length=10),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300brasil_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='tplograd',
            field=models.TextField(default=b'A', max_length=4),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='uf',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s2300cargofuncao',
            name='codcargo',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s2300cargofuncao',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300cnh',
            name='categoriacnh',
            field=models.CharField(choices=[(b'A', 'A - A'), (b'AB', 'AB - AB'), (b'AC', 'AC - AC'), (b'AD', 'AD - AD'), (b'AE', 'AE - AE'), (b'B', 'B - B'), (b'C', 'C - C'), (b'D', 'D - D'), (b'E', 'E - E')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s2300cnh',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300cnh',
            name='dtvalid',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2300cnh',
            name='nrregcnh',
            field=models.CharField(default=b'A', max_length=12),
        ),
        migrations.AlterField(
            model_name='s2300cnh',
            name='ufcnh',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s2300contato',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300contato',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300contato_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AlterField(
            model_name='s2300ctps',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300ctps',
            name='nrctps',
            field=models.CharField(default=b'A', max_length=11),
        ),
        migrations.AlterField(
            model_name='s2300ctps',
            name='seriectps',
            field=models.CharField(default=b'A', max_length=5),
        ),
        migrations.AlterField(
            model_name='s2300ctps',
            name='ufctps',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='depirrf',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='depsf',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='dtnascto',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='inctrab',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='nmdep',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='s2300_evttsvinicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300dependente_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='tpdep',
            field=models.CharField(choices=[(b'01', '01 - C\xf4njuge'), (b'02', '02 - Companheiro(a) com o(a) qual tenha filho ou viva h\xe1 mais de 5 (cinco) anos ou possua Declara\xe7\xe3o de Uni\xe3o Est\xe1vel'), (b'03', '03 - Filho(a) ou enteado(a)'), (b'04', '04 - Filho(a) ou enteado(a), universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xba grau'), (b'06', '06 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'), (b'07', '07 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xb0 grau, do(a) qual detenha a guarda judicial'), (b'09', '09 - Pais, av\xf3s e bisav\xf3s'), (b'10', '10 - Menor pobre do qual detenha a guarda judicial'), (b'11', '11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'), (b'12', '12 - Ex-c\xf4njuge'), (b'99', '99 - Agregado/Outros')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s2300exterior',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300exterior',
            name='dsclograd',
            field=models.CharField(default=b'A', max_length=100),
        ),
        migrations.AlterField(
            model_name='s2300exterior',
            name='nmcid',
            field=models.CharField(default=b'A', max_length=50),
        ),
        migrations.AlterField(
            model_name='s2300exterior',
            name='nrlograd',
            field=models.CharField(default=b'A', max_length=10),
        ),
        migrations.AlterField(
            model_name='s2300exterior',
            name='paisresid',
            field=models.TextField(default=b'A', max_length=3),
        ),
        migrations.AlterField(
            model_name='s2300exterior',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300exterior_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AlterField(
            model_name='s2300fgts',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300fgts',
            name='opcfgts',
            field=models.IntegerField(choices=[(1, '1 - Optante'), (2, '2 - N\xe3o Optante')], default=0),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='defauditiva',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='deffisica',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='defintelectual',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='defmental',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='defvisual',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='reabreadap',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300infodeficiencia_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AlterField(
            model_name='s2300infodirigentesindical',
            name='categorig',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s2300infodirigentesindical',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300infoestagiario',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300infoestagiario',
            name='dtprevterm',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2300infoestagiario',
            name='natestagio',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o Obrigat\xf3rio'), (b'O', 'O - Obrigat\xf3rio')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2300infoestagiario',
            name='nivestagio',
            field=models.IntegerField(choices=[(1, '1 - Fundamental'), (2, '2 - M\xe9dio'), (3, '3 - Forma\xe7\xe3o Profissional'), (4, '4 - Superior'), (8, '8 - Especial'), (9, '9 - M\xe3e social (Lei 7644, de 1987)')], default=0),
        ),
        migrations.AlterField(
            model_name='s2300infoestagiario',
            name='nmrazao',
            field=models.CharField(default=b'A', max_length=100),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='categorig',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='cnpjcednt',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='dtadmced',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='infonus',
            field=models.IntegerField(choices=[(1, '1 - \xd4nus do Cedente'), (2, '2 - \xd4nus do Cession\xe1rio'), (3, '3 - \xd4nus do Cedente e Cession\xe1rio')], default=0),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='matricced',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='tpregprev',
            field=models.IntegerField(choices=[(1, '1 - Regime Geral da Previd\xeancia Social - RGPS'), (2, '2 - Regime Pr\xf3prio de Previd\xeancia Social - RPPS'), (3, '3 - Regime de Previd\xeancia Social no Exterior')], default=0),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='tpregtrab',
            field=models.IntegerField(choices=[(1, '1 - CLT - Consolida\xe7\xe3o das Leis de Trabalho e legisla\xe7\xf5es trabalhistas espec\xedficas'), (2, '2 - Estatut\xe1rio')], default=0),
        ),
        migrations.AlterField(
            model_name='s2300oc',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300oc',
            name='nroc',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s2300oc',
            name='orgaoemissor',
            field=models.CharField(default=b'A', max_length=20),
        ),
        migrations.AlterField(
            model_name='s2300remuneracao',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300remuneracao',
            name='undsalfixo',
            field=models.IntegerField(choices=[(1, '1 - Por Hora'), (2, '2 - Por Dia'), (3, '3 - Por Semana'), (4, '4 - Por Quinzena'), (5, '5 - Por M\xeas'), (6, '6 - Por Tarefa'), (7, '7 - N\xe3o aplic\xe1vel - sal\xe1rio exclusivamente vari\xe1vel')], default=0),
        ),
        migrations.AlterField(
            model_name='s2300remuneracao',
            name='vrsalfx',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s2300rg',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300rg',
            name='nrrg',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s2300rg',
            name='orgaoemissor',
            field=models.CharField(default=b'A', max_length=20),
        ),
        migrations.AlterField(
            model_name='s2300ric',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300ric',
            name='nrric',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s2300ric',
            name='orgaoemissor',
            field=models.CharField(default=b'A', max_length=20),
        ),
        migrations.AlterField(
            model_name='s2300rne',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300rne',
            name='nrrne',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s2300rne',
            name='orgaoemissor',
            field=models.CharField(default=b'A', max_length=20),
        ),
        migrations.AlterField(
            model_name='s2300supervisorestagio',
            name='cpfsupervisor',
            field=models.CharField(default=b'A', max_length=11),
        ),
        migrations.AlterField(
            model_name='s2300supervisorestagio',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300supervisorestagio',
            name='nmsuperv',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='s2300supervisorestagio',
            name='s2300_infoestagiario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300supervisorestagio_s2300_infoestagiario', to='s2300.s2300infoEstagiario'),
        ),
        migrations.AlterField(
            model_name='s2300termino',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300termino',
            name='dtterm',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2300termino',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300termino_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.AlterField(
            model_name='s2300trabestrangeiro',
            name='casadobr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2300trabestrangeiro',
            name='classtrabestrang',
            field=models.IntegerField(choices=[(1, '1 - Visto permanente'), (10, '10 - Beneficiado pelo acordo entre pa\xedses do Mercosul'), (11, '11 - Dependente de agente diplom\xe1tico e/ou consular de pa\xedses que mant\xe9m conv\xeanio de reciprocidade para o exerc\xedcio de atividade remunerada no Brasil'), (12, '12 - Beneficiado pelo Tratado de Amizade, Coopera\xe7\xe3o e Consulta entre a Rep\xfablica Federativa do Brasil e a Rep\xfablica Portuguesa'), (2, '2 - Visto tempor\xe1rio'), (3, '3 - Asilado'), (4, '4 - Refugiado'), (5, '5 - Solicitante de Ref\xfagio'), (6, '6 - Residente fora do Brasil'), (7, '7 - Deficiente f\xedsico e com mais de 51 anos'), (8, '8 - Com resid\xeancia provis\xf3ria e anistiado, em situa\xe7\xe3o irregular'), (9, '9 - Perman\xeancia no Brasil em raz\xe3o de filhos ou c\xf4njuge brasileiros')], default=0),
        ),
        migrations.AlterField(
            model_name='s2300trabestrangeiro',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s2300trabestrangeiro',
            name='filhosbr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2300trabestrangeiro',
            name='s2300_evttsvinicio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2300trabestrangeiro_s2300_evttsvinicio', to='esocial.s2300evtTSVInicio'),
        ),
        migrations.DeleteModel(
            name='s2300documentos',
        ),
        migrations.DeleteModel(
            name='s2300infoComplementares',
        ),
    ]
