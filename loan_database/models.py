from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Cliente(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    telefone = models.CharField(
        max_length=16, help_text='Insira o telefone com DDD', null=True, blank=True)
    valor = models.DecimalField(
        max_digits=22, decimal_places=2, verbose_name='Valor R$', name='valor')
    juros = models.CharField(max_length=22, verbose_name='juros %',
                             help_text='Insira a porcentagem de juros')
    parcelas = models.IntegerField(default=0, blank=True, null=True)
    pagamento_mensal = models.DecimalField(
        max_digits=22, decimal_places=2, verbose_name='Valor de pagamento mensal',
        help_text='Insira o valor dos juros mensais', name='juros_mes')
    data = models.DateField(
        verbose_name='Data do empréstimo', blank=True, null=True)
    vencimento_mensal = models.DateField(verbose_name='Data de Pagamento',
                                         blank=True, null=True)
    mensalidade_paga = models.BooleanField(
        default=False, verbose_name='Mensalidade Paga', name='checkbox1')
    divida_total_paga = models.BooleanField(
        default=False, verbose_name='Dívida Total Paga', name='checkbox2')

    def save(self, *args, **kwargs):
        if self.data:
            next_month = self.data + datetime.timedelta(days=30)
            self.vencimento_mensal = next_month
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        juros = float(self.juros.strip().replace("%", "")) / 100
        self.pagamento_mensal = (
            float(self.valor) + (float(self.valor) * juros)) / self.parcelas
        if self.data:
            next_month = self.data + datetime.timedelta(days=30)
            self.vencimento_mensal = next_month
        super().save(*args, **kwargs)
