from rest_framework import serializers
from ajax.models import Perguntas

class PerguntasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Perguntas
		fields = '__all__'