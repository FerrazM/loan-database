# Generated by Django 4.1.4 on 2023-01-07 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan_database', '0005_alter_cliente_telefone_2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='telefone_1',
            new_name='telefone',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefone_2',
        ),
    ]
