# Generated by Django 4.2.15 on 2024-08-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0006_alter_empresa_contato_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga_emprego',
            name='observacao',
            field=models.TextField(blank=True, default='', verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='vaga_emprego',
            name='experiencia',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Des', 'Desejável')], max_length=3, verbose_name='Experiência'),
        ),
    ]
