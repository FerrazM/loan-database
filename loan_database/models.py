from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(
        max_length=16, help_text='Insira o telefone com DDD')
    valor = models.CharField(max_length=22, verbose_name='Valor R$')
    juros = models.CharField(max_length=6, verbose_name='juros %',
                             help_text='Insira a porcentagem de juros')
    pagamento_mensal = models.CharField(max_length=22, verbose_name='Valor de pagamento mensal',
                                        help_text='Insira o valor dos juros mensais')
    data = models.CharField(max_length=10,
                            verbose_name='Data do empréstimo', blank=True, null=True)
    vencimento_mensal = models.CharField(verbose_name='Data de Pagamento',
        max_length=10, blank=True, null=True)
    divida_total_paga = models.BooleanField(default=False,
                                            verbose_name='Dívida paga')
