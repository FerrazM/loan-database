# Generated by Django 4.1.5 on 2023-01-23 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan_database', '0028_rename_data_cliente_data_emprestimo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='data_emprestimo',
            new_name='data',
        ),
    ]
