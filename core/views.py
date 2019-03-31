import random
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from graficos.models import Pontuacao

def index(request):
	return render(request, 'index.html')


@login_required(login_url='/admin/')
def sorteio(request):
	lista_nomes = list(set(Pontuacao.objects.values_list('nome')))
	escolhido = random.choice(lista_nomes)

	return render(request, 'sorteio.html', {'lista_nomes': lista_nomes, 'escolhido': escolhido}, )
# Create your views here.
