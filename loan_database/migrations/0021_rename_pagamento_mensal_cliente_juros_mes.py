# Generated by Django 4.1.4 on 2023-01-20 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan_database', '0020_alter_cliente_vencimento_mensal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='pagamento_mensal',
            new_name='juros_mes',
        ),
    ]
