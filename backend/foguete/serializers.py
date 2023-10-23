
from rest_framework import serializers

from .models import DadosVoo


class DadosVooSerializer(serializers.ModelSerializer):

    class Meta:
        model = DadosVoo
        fields = '__all__'
