from django.contrib import admin

from garagem.models import Categoria, Marca, Carro, Acessorio, Cor

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Carro)
admin.site.register(Acessorio)
admin.site.register(Cor)

