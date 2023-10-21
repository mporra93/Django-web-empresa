from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name='Title',max_length=200)
    content = RichTextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion') # auto_now_add -> al crearse
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion') # auto_now -> cada vez que se ejecuta una instancia


    def __str__(self):
        return self.title