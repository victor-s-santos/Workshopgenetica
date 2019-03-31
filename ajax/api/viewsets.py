from rest_framework.viewsets import ModelViewSet
from ajax.models import Perguntas
from .serializers import PerguntasSerializer

class PerguntasViewSet(ModelViewSet):
	serializer_class = PerguntasSerializer

	def get_queryset(self):
		return Perguntas.objects.all()