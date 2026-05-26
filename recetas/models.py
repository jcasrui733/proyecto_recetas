from django.db import models

# Create your models here.

class Receta(models.Model):
    titulo = models.CharField(max_length = 100)
    ingredientes = models.TextField( blank=False,null=False)
    pasos_elaboracion = models.TextField(blank=False,null=False)
    tiempo_preparacion = models.PositiveIntegerField()
    Categoria = models.CharField(max_length=100,)
    Autor = models.CharField(max_length=100)
    Fecha_creacion = models.DateTimeField(auto_now_add= True)