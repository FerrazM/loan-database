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
        verbose_name='Data de pagamento', blank=True, null=True)
    vencimento_mensal = models.DateField(verbose_name='Vencimento',
                                         blank=True, null=True)
    mensalidade_paga = models.BooleanField(
        default=False, verbose_name='Mensalidade Paga', name='checkbox1')
    divida_total_paga = models.BooleanField(
        default=False, verbose_name='Dívida Total Paga', name='checkbox2')

    def pagar_parcela(self):
        if not self.mensalidade_paga:
            self.parcelas_pagas += 1
            self.mensalidade_paga = True
            self.save()

    @property
    def parcelas_restantes(self):
        return self.parcelas - self.parcelas_pagas

    def parcelas_pagas_string(self):
        return f"{self.parcelas_pagas}/{self.parcelas} parcelas pagas"
