# Generated by Django 3.2.5 on 2023-01-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_database', '0007_alter_cliente_data_alter_cliente_juros_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='divida_total_paga',
            field=models.BooleanField(default=False, verbose_name='Dívida paga'),
        ),
    ]