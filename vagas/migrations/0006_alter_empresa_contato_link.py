# Generated by Django 4.2.2 on 2023-07-28 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0005_empresa_contato_link_empresa_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='contato_link',
            field=models.BooleanField(default=False, verbose_name='Contato via link'),
        ),
    ]
