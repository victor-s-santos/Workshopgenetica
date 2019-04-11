from django.utils import timezone
from django import forms
from .models import *

x = timezone.now().strftime("%Y")
class PontuacaoForm(forms.ModelForm):
	class Meta:
		model = Pontuacao
		fields = ('palestrante', 'pontuacao', 'nome', 'email', 'sugestao')
	
	def __init__(self, *args, **kwargs):
		super(PontuacaoForm, self).__init__(*args, **kwargs)
		self.fields['palestrante'].queryset = Palestrante.objects.filter(data__year=x)
		#assim somente o palestrante do ano atual vai estar "avaliável"

class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		fields = '__all__'

class PontuacaoMinicursosForm(forms.ModelForm):
	class Meta:
		model = PontuacaoMinicursos
		fields = ('minicurso', 'nome', 'email', 'pontuacao', 'sugestao')

	def __init__(self, *args, **kwargs):
		super(PontuacaoMinicursosForm, self).__init__(*args, **kwargs)
		self.fields['minicurso'].queryset = MiniCursos.objects.filter(data__year=x)