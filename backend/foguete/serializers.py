
from rest_framework import serializers

from .models import Voo, Instante, Eixo


class VooSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voo
        model = Instante
        model = Eixo
        fields = '__all__'
