from django import forms
from .models import Servico, BeneficioServico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
        widgets = {
            'descricao_curta': forms.Textarea(attrs={'rows': 3}),
            'caracteristicas': forms.Textarea(attrs={'rows': 3}),
        }


class BeneficioServicoForm(forms.ModelForm):
    class Meta:
        model = BeneficioServico
        fields = '__all__'