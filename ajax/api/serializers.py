from rest_framework.serializers import ModelSerializer
from ajax.models import Perguntas

class PerguntasSerializer(ModelSerializer):
	class Meta:
		model = Perguntas
		fields = ('id', 'texto')