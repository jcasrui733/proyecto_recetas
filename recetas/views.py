from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Receta
from .forms import RecetaForm, ComentarioForm


class ListaRecetasView(ListView):
    model = Receta
    template_name = "recetas/lista_recetas.html"
    context_object_name = "recetas"


class DetalleRecetaView(DetailView):
    model = Receta
    template_name = "recetas/detalles_recetas.html"
    context_object_name = "receta"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_comentario"] = ComentarioForm()
        return context
    
def agregar_comentario(request,pk):
    receta = get_object_or_404(Receta, pk=pk)

    if request.method == "POST" and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user 
            comentario.reseta_asociada = receta
            comentario.save()
    return redirect("detalles_receta", pk=pk)



class CrearRecetaView(LoginRequiredMixin,CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = "recetas/crear_recetas.html"
    success_url = reverse_lazy("lista_recetas")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class EditarRecetaView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = "recetas/crear_recetas.html"
    success_url = reverse_lazy("lista_recetas")

    def test_func(self):
        receta = self.get_object()
        return self.request.user == receta.autor

    
class EliminarRecetaView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Receta
    template_name = "recetas/eliminar_receta.html"
    success_url = reverse_lazy("lista_recetas")
    def test_func(self):
        receta = self.get_object()
        return self.request.user == receta.autor
