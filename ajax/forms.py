from django import forms
from .models import Perguntas

class PerguntasForm(forms.ModelForm):
	class Meta:
		model = Perguntas
		fields = ('texto',)