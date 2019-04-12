import random
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from graficos.models import Pontuacao, Evento

def index(request):
	return render(request, 'index.html')


@login_required(login_url='/admin/')
def sorteio(request):
	lista_pontuacao = Pontuacao.objects.all()
	lista_evento = Evento.objects.all()
	lista_nomes = list(set(Pontuacao.objects.values_list('nome')))
	escolhido = random.choice(lista_nomes)
	lista_nomes2 = list(set(Evento.objects.values_list('nome')))
	escolhido2 = random.choice(lista_nomes2)
	escolhido3 = random.choice(lista_nomes)


	return render(request, 'sorteio.html', 
		{'lista_nomes': lista_nomes, 
		'escolhido': escolhido, 
		'lista_nomes2': lista_nomes2,
		'escolhido2': escolhido2,
		'lista_pontuacao': lista_pontuacao,
		'lista_evento': lista_evento,
		'escolhido3': escolhido3})
# Create your views here.
