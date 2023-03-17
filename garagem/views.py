from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Marca, Carro
from garagem.serializers import CategoriaSerializer, MarcaSerializer, CarroSerializer, CarroDetailSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CarroDetailSerializer
        return CarroSerializer