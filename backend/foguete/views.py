from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Voo
from .serializers import VooSerializer


class DadosVooViewSet(viewsets.ModelViewSet):

    serializer_class = VooSerializer
    queryset = Voo.objects.all()
