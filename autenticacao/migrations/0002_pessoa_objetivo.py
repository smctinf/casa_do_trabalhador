# Generated by Django 4.2.2 on 2023-08-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='objetivo',
            field=models.CharField(blank=True, max_length=380, null=True, verbose_name='Objetivo'),
        ),
    ]