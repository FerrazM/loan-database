# Generated by Django 4.1.4 on 2023-02-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_database', '0005_cliente_parcelas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='parcelas',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
