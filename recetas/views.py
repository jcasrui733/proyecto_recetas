from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Receta
from .forms import RecetaForm


class ListaRecetasView(ListView):
    model = Receta
    template_name = "recetas/lista_recetas.html"
    context_object_name = "recetas"


class DetalleRecetaView(DetailView):
    model = Receta
    template_name = "recetas/detalles_recetas.html"
    context_object_name = "receta"


class CrearRecetaView(LoginRequiredMixin,CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = "recetas/crear_recetas.html"
    success_url = reverse_lazy("lista_recetas")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)