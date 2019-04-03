from django.db import models
from django.utils import timezone

class Perguntas(models.Model):
	texto = models.TextField()
	data = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Pergunta'
		verbose_name_plural = 'Perguntas'

	def publish(self):
		#self.data = timezone.now()
		self.save()

	def __str__(self):
		return self.texto