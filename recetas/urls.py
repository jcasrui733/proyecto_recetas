from django.urls import path
from .views import ListaRecetasView, DetalleRecetaView, CrearRecetaView,EditarRecetaView,EliminarRecetaView

urlpatterns = [
    path("",ListaRecetasView.as_view(), name= "lista_recetas"),
    path("receta/<int:pk>/",DetalleRecetaView.as_view(), name = "detalles_receta"),
    path("crear/", CrearRecetaView.as_view(), name = "crear_receta"),
    path("editar/<int:pk>/",EditarRecetaView.as_view(), name="editar_receta"),
    path("eliminar/<int:pk>/", EliminarRecetaView.as_view(), name="eliminar_receta"),
]