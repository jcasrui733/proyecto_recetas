from django import forms
from .models import Receta , Comentario


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ["titulo","ingredientes","pasos_elaboracion", "tiempo_preparacion"]


class ComentarioForm(forms.ModelForm):
     class Meta:
        model = Comentario
        fields = ["contenido"]