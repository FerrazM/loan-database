# Generated by Django 3.2.5 on 2023-01-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_database', '0018_auto_20230118_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Data do empréstimo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='vencimento_mensal',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
