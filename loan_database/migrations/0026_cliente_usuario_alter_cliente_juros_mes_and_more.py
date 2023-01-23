# Generated by Django 4.1.4 on 2023-01-23 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loan_database', '0025_auto_20230120_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='juros_mes',
            field=models.CharField(help_text='Insira o valor dos juros mensais', max_length=22, verbose_name='Valor de pagamento mensal'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='valor',
            field=models.CharField(max_length=22, verbose_name='Valor R$'),
        ),
    ]