from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name='Nombre Clave', max_length=100, unique=True) # sirve para claves
    name = models.CharField(verbose_name='Red social',max_length=200)
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion') # auto_now_add -> al crearse
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion') # auto_now -> cada vez que se ejecuta una instancia

    def __str__(self):
        return self.name