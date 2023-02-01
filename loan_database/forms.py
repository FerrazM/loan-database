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
        self.fields['valor'].widget.attrs.update({'class': 'mask-valor'})
        self.fields['juros'].widget.attrs.update({'class': 'mask-juros'})
        self.fields['juros_mes'].widget.attrs.update(
            {'class': 'mask-pagamento'})
        self.fields['data'].widget.attrs.update({'class': 'mask-data'})
        self.fields['vencimento_mensal'].widget.attrs.update(
            {'class': 'mask-vencimento'})
        self.fields['usuario'].widget = forms.HiddenInput()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.mensalidade_paga:
            self.fields['juros_mes'].widget.attrs['class'] = 'green-field'
        else:
            self.fields['juros_mes'].widget.attrs['class'] = 'red-field'
