from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from .models import Perguntas
from .forms import PerguntasForm
from .serializers import PerguntasSerializer

class Get_Perguntas_List(APIView):
	def get(self, request):
		perguntas = Perguntas.objects.all()
		serialized = PerguntasSerializer(perguntas, many=True)
		return Response(serialized.data)

def ajax_index(request):
	if request.method == "POST":
		form = PerguntasForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.data = timezone.now()
			post.save()
			return redirect('ajax_index')
	else:
		form = PerguntasForm()
	return render(request, 'ajax_index.html', {'form': form})
# Create your views here.
