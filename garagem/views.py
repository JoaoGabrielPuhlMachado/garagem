from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Marca, Carro, Acessorio, Cor
from garagem.serializers import CategoriaSerializer, MarcaSerializer, CarroSerializer, CarroDetailSerializer, AcessorioSerializer, CorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = AcessorioSerializer

class CorViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = CorSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CarroDetailSerializer
        return CarroSerializer