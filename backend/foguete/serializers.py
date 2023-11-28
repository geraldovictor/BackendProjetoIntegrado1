
from rest_framework import serializers

from .models import Voo, Instante


class VooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voo
        fields = '__all__'

class InstanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instante
        fields = '__all__'