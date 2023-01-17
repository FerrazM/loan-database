from django.db import models
from datetime import datetime


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=16)
    valor = models.CharField(max_length=22)
    juros = models.CharField(max_length=6, verbose_name='juros %',
                             help_text='Insira a porcentagem de juros')
    pagamento_mensal = models.CharField(max_length=22, verbose_name='Valor de pagamento mensal',
                                        help_text='Insira o valor dos juros mensais')
    data = models.DateField(max_length=10, default=datetime.now,
                            verbose_name='Data do empréstimo')
    vencimento_mensal = models.DateField(default=datetime.now,
                                         max_length=10)
    divida_total_paga = models.BooleanField(default=False,
                                            verbose_name='Dívida paga')
