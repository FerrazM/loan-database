from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class Cliente(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    telefone = models.CharField(
        max_length=16, help_text='Insira o telefone com DDD', null=True, blank=True)
    endereco = models.TextField(
        max_length=300, null=True, blank=True, verbose_name='Endereço')
    valor = models.DecimalField(
        max_digits=22, decimal_places=2, verbose_name='Valor R$', name='valor')
    juros = models.CharField(max_length=22, verbose_name='juros %',
                             help_text='Insira a porcentagem de juros')
    parcelas = models.IntegerField(default=1, blank=True, null=True)
    parcelas_pagas = models.IntegerField(default=0, blank=True, null=True)
    pagamento_mensal = models.DecimalField(
        max_digits=22, decimal_places=2, verbose_name='Valor de pagamento mensal',
        help_text='Insira o valor dos juros mensais', name='juros_mes')
    data_emprestimo = models.DateField(
        blank=True, null=True, verbose_name='Data do empréstimo')
    data = models.DateField(
        verbose_name='Pagou em:', blank=True, null=True)
    vencimento_mensal = models.DateField(verbose_name='Vence:',
                                         blank=True, null=True)
    mensalidade_paga = models.BooleanField(
        default=False, verbose_name='Mensalidade Paga', name='checkbox1')
    divida_total_paga = models.BooleanField(
        default=False, verbose_name='Dívida Total Paga', name='checkbox2')

    def save(self, *args, **kwargs):
        if self.data:
            self.data = self.vencimento_mensal + \
                relativedelta(months=-1) if self.data else None
        super().save(*args, **kwargs)

    def pagar_parcela(self):
        if not self.checkbox1:
            self.parcelas_pagas += 1
            self.checkbox1 = True
            self.save()

    @property
    def parcelas_restantes(self):
        return self.parcelas - self.parcelas_pagas

    def parcelas_pagas_string(self):
        return f"{self.parcelas_pagas}/{self.parcelas} parcelas pagas"
