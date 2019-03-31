from django.db import models
from django.utils import timezone

class Perguntas(models.Model):
	texto = models.TextField()
	data = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Pergunta'
		verbose_name_plural = 'Perguntas'
