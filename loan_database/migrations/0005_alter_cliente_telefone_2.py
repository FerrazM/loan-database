# Generated by Django 4.1.4 on 2023-01-07 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_database', '0004_alter_cliente_vencimento_mensal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone_2',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
