# Generated by Django 4.2.2 on 2023-08-01 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=14, null=True, unique=True, verbose_name='CPF')),
                ('telefone', models.CharField(max_length=15, null=True, verbose_name='Telefone')),
                ('dt_nascimento', models.DateField(null=True, verbose_name='Data de nascimento')),
                ('bairro', models.CharField(max_length=64, null=True, verbose_name='Bairro')),
                ('endereco', models.CharField(max_length=128, null=True, verbose_name='Endereco')),
                ('complemento', models.CharField(blank=True, max_length=128, null=True, verbose_name='Complemento')),
                ('cep', models.CharField(max_length=9, null=True, verbose_name='CEP')),
                ('dt_inclusao', models.DateField(auto_now_add=True, verbose_name='Data de inclusão')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]