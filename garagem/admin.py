from django.contrib import admin

from garagem.models import Categoria, Marca, Veiculo, Acessorio, Cor

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Acessorio)
admin.site.register(Cor)
