from django.db.models.signals import pre_save
from django.dispatch import receiver
from loan_database.models import Cliente
import datetime


@receiver(pre_save, sender=Cliente)
def check_uncheck_checkbox1(sender, instance, **kwargs):
    today = datetime.date.today()
    if instance.vencimento_mensal < today:
        instance.mensalidade_paga = False
