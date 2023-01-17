from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
    self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})
    self.fields['vencimento_data'].widget.attrs.update({'class': 'mask-data'})
    self.fields['vencimento_mensal'].widget.attrs.update(
        {'class': '.mask-vencimento'})
