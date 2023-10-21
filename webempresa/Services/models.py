from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(default=" ", verbose_name='Content')
    image = models.ImageField(verbose_name='Imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion') # auto_now_add -> al crearse
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion') # auto_now -> cada vez que se ejecuta una instancia
    Url = models.URLField(verbose_name='url', null=True, blank=True)
        

    def __str__(self):
        return self.title