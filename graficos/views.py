import json, random
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Avg
from django.utils import timezone
from .models import Pontuacao, Palestrante, Evento, MiniCursos, PontuacaoMinicursos
from .forms import *
from django.contrib.auth.decorators import login_required


def grafico_index(request):
	return render(request, 'grafico_index.html')

@login_required(login_url='/admin/')	
def grafico_palestrantes(request):
	d = timezone.now()
	x = d.strftime("%Y")
	#----------------#
	try:
		palestrante1 = Palestrante.objects.filter(id=1)
		palestrante1 = [obj.nome for obj in palestrante1]
	except:
		palestrante1 = 'Palestrante'

	try:	
		palestrante2 = Palestrante.objects.filter(id=2)
		palestrante2 = [obj.nome for obj in palestrante2]
	except:
		palestrante2 = 'Palestrante'

	try:
		palestrante3 = Palestrante.objects.filter(id=3)
		palestrante3 = [obj.nome for obj in palestrante3]
	except:
		palestrante3 = 'Palestrante'
	

	try:
		pontuacao1 = float(Pontuacao.objects.filter(palestrante=1, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao1 = 0
	try:
		pontuacao2 = float(Pontuacao.objects.filter(palestrante=2, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao2 = 0
	try:
		pontuacao3 = float(Pontuacao.objects.filter(palestrante=3, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao3 = 0
	
	context = {
		'palestrante1' : json.dumps(palestrante1),
		'pontuacao1': json.dumps(pontuacao1),
		'palestrante2' : json.dumps(palestrante2),
		'pontuacao2': json.dumps(pontuacao2),
		'palestrante3' : json.dumps(palestrante3),
		'pontuacao3': json.dumps(pontuacao3)
	}


	return render(request, 'grafico_palestrantes.html', context)

def avalia(request):
	d = timezone.now()
	x = d.strftime("%Y")
	if request.method == "POST":
		form = PontuacaoForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('index')
	else:
		form = PontuacaoForm()
	return render(request, 'avalia_palestrante.html', {'form': form})

def avalia_evento(request):
	if request.method == "POST":
		form = EventoForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('index')
	else:
		form = EventoForm()
	return render(request, 'avalia_evento.html', {'form': form})

def avalia_minicurso(request):
	if request.method == "POST":
		form = PontuacaoMinicursosForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('index')
	else:
		form = PontuacaoMinicursosForm()
	return render(request, 'avalia_minicurso.html', {'form': form})


@login_required(login_url='/admin/')	
def grafico_geral(request):
	d = timezone.now()
	x = d.strftime("%Y")

	try:
		organizacao = Evento.objects.filter(data__year=x).values('organizacao').aggregate(Avg('organizacao')).get('organizacao__avg')
	except:
		organizacao = 0

	try:
		limpeza = Evento.objects.filter(data__year=x).values('limpeza').aggregate(Avg('limpeza')).get('limpeza__avg')
	except:
		limpeza = 0

	try:
		coffe_break = Evento.objects.filter(data__year=x).values('coffe_break').aggregate(Avg('coffe_break')).get('coffe_break__avg')
	except:
		coffe_break = 0

	try:
		tema = Evento.objects.filter(data__year=x).values('tema').aggregate(Avg('tema')).get('tema__avg')
	except:
		tema = 0

	context = {
		'organizacao' : json.dumps(organizacao),
		'limpeza': json.dumps(limpeza),
		'coffe_break' : json.dumps(coffe_break),
		'tema': json.dumps(tema),
	}


	return render(request, 'grafico_geral.html', context)

