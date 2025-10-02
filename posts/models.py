from django.db import models

# Create your models here.
# Creamos la tabla posts  con : Titulo , contenido y fecha de publicacion
class Post (models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
 
