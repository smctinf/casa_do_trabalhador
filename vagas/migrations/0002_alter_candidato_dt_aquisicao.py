# Generated by Django 3.2.13 on 2022-08-23 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='dt_aquisicao',
            field=models.CharField(default='', max_length=10),
        ),
    ]