from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Voo, Instante
from .serializers import VooSerializer, InstanteSerializer


class VooViewSet(viewsets.ModelViewSet):
    serializer_class = VooSerializer
    queryset = Voo.objects.all()

class InstanteViewSet(viewsets.ModelViewSet):
    serializer_class = InstanteSerializer
    queryset = Instante.objects.all()
