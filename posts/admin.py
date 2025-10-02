from django.contrib import admin

# Register your models here.
#Registramos el modelo para poder crear posts desde el panel de django admin
from django.contrib import admin 
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields =('titulo', 'contenido')
    
