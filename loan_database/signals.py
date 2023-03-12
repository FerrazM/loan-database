from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Cliente


@receiver(post_save, sender=Cliente)
def check_uncheck_checkbox1(sender, instance, **kwargs):
    today = timezone.now().date()
    if instance.vencimento_mensal < today:
        instance.checkbox1 = False
        instance.save(update_fields=['checkbox1'])
