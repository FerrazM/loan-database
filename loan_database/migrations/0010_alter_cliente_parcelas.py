# Generated by Django 4.1.5 on 2023-02-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_database', '0009_cliente_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='parcelas',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
