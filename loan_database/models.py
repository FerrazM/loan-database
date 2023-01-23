from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(
        max_length=16, help_text='Insira o telefone com DDD')
    valor = models.DecimalField(
        max_digits=22, decimal_places=2, verbose_name='Valor R$', name='valor')
    juros = models.CharField(max_length=22, verbose_name='juros %',
                             help_text='Insira a porcentagem de juros')
    pagamento_mensal = models.DecimalField(
        max_digits=22, decimal_places=2, verbose_name='Valor de pagamento mensal',
        help_text='Insira o valor dos juros mensais', name='juros_mes')
    data = models.DateField(
        verbose_name='Data do empréstimo', blank=True, null=True)
    vencimento_mensal = models.DateField(verbose_name='Data de Pagamento',
                                         blank=True, null=True)
    divida_total_paga = models.BooleanField(default=False,
                                            verbose_name='Dívida paga')
