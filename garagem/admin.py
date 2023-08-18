from django.contrib import admin

from garagem.models import Categoria, Marca, Veiculo, Acessorio, Cor

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade')
    search_fields = ('nome', 'nacionalidade')
    list_filter = ('nome',)
    ordering = ('nome', 'nacionalidade')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

@admin.register(Acessorio)
class AcessorioAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'categoria', 'marca', 'cor')
    search_fields = ('descricao', 'marca__nome', 'categoria__descricao', 'acessorio__descricao', 'acessorio__descricao')
    list_filter = ('categoria', 'marca', 'acessorio', 'cor' )
    ordering = ('descricao', 'marca', 'categoria', 'cor', 'acessorio')
    list_per_page = 25