# Generated by Django 4.1.5 on 2023-02-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_database', '0008_alter_cliente_parcelas_pagas'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Endereço'),
        ),
    ]