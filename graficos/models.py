from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Palestrante(models.Model):
	nome = models.CharField(max_length=200)
	id = models.IntegerField(primary_key=True)
	data = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = 'Palestrante'
		verbose_name_plural = 'Palestrantes'

	def __str__(self):
		return self.nome

class Pontuacao(models.Model):
	palestrante = models.ForeignKey(Palestrante, related_name='palesta', on_delete=models.CASCADE)
	pontuacao = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])
	nome = models.CharField(max_length=800)
	email = models.EmailField(max_length=200, blank=False, null=False)
	sugestao = models.TextField(blank=True, null=True)
	data = models.DateField(auto_now_add=True)
	id = models.AutoField(primary_key=True)
	class Meta:
		unique_together = ('palestrante', 'email')
		verbose_name = 'Pontuação'
		verbose_name_plural = 'Pontuações'

	def __str__(self):
		return str(self.pontuacao)

class Evento(models.Model):
	nome = models.CharField(blank=False, null=False, max_length=200)
	limpeza = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])
	organizacao = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])
	coffe_break = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])
	tema = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])
	email = models.EmailField(max_length=200, blank=False, null=False, unique=True)
	sugestao = models.TextField(blank=True, null=True)
	data = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = 'Avaliação do Evento'
		verbose_name_plural = 'Avaliações do Evento'

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome

class MiniCursos(models.Model):
	minicurso = models.CharField(blank=False, null=False, max_length=300)
	ministrante = models.CharField(blank=False, null=False, max_length=300)
	data = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = 'mini_curso'
		verbose_name_plural = 'mini_cursos'

	def __str__(self):
		return self.minicurso

class PontuacaoMinicursos(models.Model):
	minicurso = models.ForeignKey(MiniCursos, on_delete=models.CASCADE)
	nome = models.CharField(blank=False, null=False, max_length=200)
	email = models.EmailField(max_length=200, blank=False, null=False, unique=True)
	clareza = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])
	tempo = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])
	tema = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])
	relevancia = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])
	data = models.DateField(auto_now_add=True)
	
	class Meta:
		unique_together = ('minicurso', 'email')
		verbose_name = 'Pontuação Minicurso'
		verbose_name_plural = 'Pontuações Minicurso'

	def __str__(self):
		return str(self.minicurso)