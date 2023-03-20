from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import CategoriaViewSet, MarcaViewSet, CarroViewSet, AcessorioViewSet, CorViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"carros", CarroViewSet)
router.register(r"acessorios", AcessorioViewSet)
router.register(r"cores", CorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
