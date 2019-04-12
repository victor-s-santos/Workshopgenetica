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
		palestrante4 = Palestrante.objects.filter(id=4)
		palestrante4 = [obj.nome for obj in palestrante4]
	except:
		palestrante4 = 'Palestrante'

	try:	
		palestrante5 = Palestrante.objects.filter(id=5)
		palestrante5 = [obj.nome for obj in palestrante5]
	except:
		palestrante5 = 'Palestrante'

	try:
		palestrante6 = Palestrante.objects.filter(id=6)
		palestrante6 = [obj.nome for obj in palestrante6]
	except:
		palestrante6 = 'Palestrante'

	try:
		palestrante7 = Palestrante.objects.filter(id=7)
		palestrante7 = [obj.nome for obj in palestrante7]
	except:
		palestrante7 = 'Palestrante'

	try:
		palestrante8 = Palestrante.objects.filter(id=8)
		palestrante8 = [obj.nome for obj in palestrante8]
	except:
		palestrante8 = 'Palestrante'

	try:
		palestrante9 = Palestrante.objects.filter(id=9)
		palestrante9 = [obj.nome for obj in palestrante9]
	except:
		palestrante9 = 'Palestrante'

	try:
		palestrante10 = Palestrante.objects.filter(id=10)
		palestrante10 = [obj.nome for obj in palestrante10]
	except:
		palestrante10 = 'Palestrante'


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
	
	try:
		pontuacao4 = float(Pontuacao.objects.filter(palestrante=4, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao4 = 0
	
	try:
		pontuacao5 = float(Pontuacao.objects.filter(palestrante=5, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao5 = 0
	
	try:
		pontuacao6 = float(Pontuacao.objects.filter(palestrante=6, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao6 = 0

	try:
		pontuacao7 = float(Pontuacao.objects.filter(palestrante=7, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao7 = 0

	try:
		pontuacao8 = float(Pontuacao.objects.filter(palestrante=8, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao8 = 0

	try:
		pontuacao9 = float(Pontuacao.objects.filter(palestrante=9, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao9 = 0

	try:
		pontuacao10 = float(Pontuacao.objects.filter(palestrante=10, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao10 = 0
	
	context = {
		'palestrante1' : json.dumps(palestrante1),
		'pontuacao1': json.dumps(pontuacao1),
		'palestrante2' : json.dumps(palestrante2),
		'pontuacao2': json.dumps(pontuacao2),
		'palestrante3' : json.dumps(palestrante3),
		'pontuacao3': json.dumps(pontuacao3),
		'palestrante4' : json.dumps(palestrante4),
		'pontuacao4': json.dumps(pontuacao4),
		'palestrante5' : json.dumps(palestrante5),
		'pontuacao5': json.dumps(pontuacao5),
		'palestrante6' : json.dumps(palestrante6),
		'pontuacao6': json.dumps(pontuacao6),
		'palestrante7' : json.dumps(palestrante7),
		'pontuacao7': json.dumps(pontuacao7),
		'palestrante8' : json.dumps(palestrante8),
		'pontuacao8': json.dumps(pontuacao8),
		'palestrante9' : json.dumps(palestrante9),
		'pontuacao9': json.dumps(pontuacao9),
		'palestrante10' : json.dumps(palestrante10),
		'pontuacao10': json.dumps(pontuacao10),		
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
		divulgacao = Evento.objects.filter(data__year=x).values('divulgacao').aggregate(Avg('divulgacao')).get('divulgacao__avg')
	except:
		divulgacao = 0

	try:
		coffe_break = Evento.objects.filter(data__year=x).values('coffe_break').aggregate(Avg('coffe_break')).get('coffe_break__avg')
	except:
		coffe_break = 0

	try:
		palestras = Evento.objects.filter(data__year=x).values('palestras').aggregate(Avg('palestras')).get('palestras__avg')
	except:
		palestras = 0

	try:
		open_lab = Evento.objects.filter(data__year=x).values('open_lab').aggregate(Avg('open_lab')).get('open_lab__avg')
	except:
		open_lab = 0

	try:
		indicacao = Evento.objects.filter(data__year=x).values('indicacao').aggregate(Avg('indicacao')).get('indicacao__avg')
	except:
		indicacao = 0

	try:
		retorno = Evento.objects.filter(data__year=x).values('retorno').aggregate(Avg('retorno')).get('retorno__avg')
	except:
		retorno = 0

	context = {
		'organizacao' : json.dumps(organizacao),
		'divulgacao': json.dumps(divulgacao),
		'coffe_break' : json.dumps(coffe_break),
		'palestras': json.dumps(palestras),
		'open_lab' : json.dumps(open_lab),
		'indicacao' : json.dumps(indicacao),
		'retorno' : json.dumps(retorno),
	}


	return render(request, 'grafico_geral.html', context)

@login_required(login_url='/admin/')	
def grafico_minicurso(request):
	d = timezone.now()
	x = d.strftime("%Y")

	try:
		minicurso1 = MiniCursos.objects.filter(id=1)
		minicurso1 = [obj.minicurso for obj in minicurso1]
	except:
		minicurso1 = 'Minicurso1'

	try:	
		minicurso2 = MiniCursos.objects.filter(id=2)
		minicurso2 = [obj.minicurso for obj in minicurso2]
	except:
		minicurso2 = 'Minicurso2'

	try:
		minicurso3 = MiniCursos.objects.filter(id=3)
		minicurso3 = [obj.minicurso for obj in minicurso3]
	except:
		minicurso3 = 'Minicurso3'

	try:	
		minicurso4 = MiniCursos.objects.filter(id=4)
		minicurso4 = [obj.minicurso for obj in minicurso4]
	except:
		minicurso4 = 'Minicurso4'

	try:	
		minicurso5 = MiniCursos.objects.filter(id=5)
		minicurso5 = [obj.minicurso for obj in minicurso5]
	except:
		minicurso5 = 'Minicurso5'



	try:
		pontuacao1 = float(PontuacaoMinicursos.objects.filter(minicurso=1, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao1 = 0
	
	try:
		pontuacao2 = float(PontuacaoMinicursos.objects.filter(minicurso=2, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao2 = 0

	try:
		pontuacao3 = float(PontuacaoMinicursos.objects.filter(minicurso=3, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao3 = 0
	
	try:
		pontuacao4 = float(PontuacaoMinicursos.objects.filter(minicurso=4, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao4 = 0

	try:
		pontuacao5 = float(PontuacaoMinicursos.objects.filter(minicurso=5, data__year=x).aggregate(Avg('pontuacao')).get('pontuacao__avg'))
	except:
		pontuacao5 = 0


	context = {
		'minicurso1' : json.dumps(minicurso1),
		'pontuacao1': json.dumps(pontuacao1),
		
		'minicurso2' : json.dumps(minicurso2),
		'pontuacao2': json.dumps(pontuacao2),
		
		'minicurso3' : json.dumps(minicurso3),
		'pontuacao3': json.dumps(pontuacao3),
		
		'minicurso4' : json.dumps(minicurso4),
		'pontuacao4': json.dumps(pontuacao4),
		
		'minicurso5' : json.dumps(minicurso5),
		'pontuacao5': json.dumps(pontuacao5),		
	}

	return render(request, 'grafico_minicurso.html', context)