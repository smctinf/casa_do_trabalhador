# Generated by Django 3.1.4 on 2022-10-07 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0004_auto_20220930_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='dt_atualizacao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data da última atualização do candidato'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='dt_inclusao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de inclusão do candidato'),
        ),
    ]