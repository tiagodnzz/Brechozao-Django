from django import forms
from website.models import Pedido

def PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'nome',
            'email',
            'cartao',
            'pagamento',
        ]
