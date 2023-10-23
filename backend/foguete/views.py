from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import DadosVoo
from .serializers import DadosVooSerializer


class DadosVooViewSet(viewsets.ModelViewSet):

    serializer_class = DadosVooSerializer
    queryset = DadosVoo.objects.all()
