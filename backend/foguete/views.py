from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Voo, Instante
from .serializers import VooSerializer, InstanteSerializer, CountElementsSerializer


class CountElementsView(APIView):
    def get(self, request, format=None):
        # Get the count of elements in the Voo model
        voo_count = Voo.objects.count()

        # Serialize the response
        serializer = CountElementsSerializer({'voo_count': voo_count})
        return Response(serializer.data, status=status.HTTP_200_OK)

class VooViewSet(viewsets.ModelViewSet):
    serializer_class = VooSerializer
    queryset = Voo.objects.all()

class InstanteViewSet(viewsets.ModelViewSet):
    serializer_class = InstanteSerializer
    queryset = Instante.objects.all()