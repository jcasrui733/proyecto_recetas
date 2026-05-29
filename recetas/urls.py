from django.urls import path
from .views import ListaRecetasView, DetalleRecetaView, CrearRecetaView

urlpatterns = [
    path("",ListaRecetasView.as_view(), name= "lista_recetas"),
    path("receta/<int:pk>/",DetalleRecetaView.as_view(), name = "detalles_receta"),
    path("crear/", CrearRecetaView.as_view(), name = "crear_receta")
]