from rest_framework.serializers import ModelSerializer

from garagem.models import Categoria, Marca, Carro, Acessorio, Cor

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class CorSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"

class CarroDetailSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"
        depth = 1