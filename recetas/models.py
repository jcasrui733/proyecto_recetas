from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True,null =True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    titulo = models.CharField(max_length = 100)
    ingredientes = models.TextField( blank=False,null=False)
    pasos_elaboracion = models.TextField(blank=False,null=False)
    tiempo_preparacion = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, related_name="categoria")
    autor = models.ForeignKey(User, on_delete= models.CASCADE, related_name="autor")
    fecha_creacion = models.DateTimeField(auto_now_add= True)
    
    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.titulo





class Comentario(models.Model):
    contenido = models.TextField(blank=True, null=False)
    autor = models.ForeignKey(User,on_delete=models.CASCADE, related_name="autor")
    reseta_asociada = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name="recetas")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return f" Comentario de {self.autor.username} en {self.receta.titulo}"
    


