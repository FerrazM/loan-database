from django.forms import ModelForm
from .models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cpf'].widget.attrs.update({'class': 'cpf'})