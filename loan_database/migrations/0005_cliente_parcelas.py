# Generated by Django 4.1.5 on 2023-02-01 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_database', '0004_rename_mensalidade_paga_cliente_checkbox1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='parcelas',
            field=models.IntegerField(default=1),
        ),
    ]
