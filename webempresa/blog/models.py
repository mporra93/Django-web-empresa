from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion') # auto_now_add -> al crearse
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion') # auto_now -> cada vez que se ejecuta una instancia

    def __str__(self):
        return self.name
    


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Content')
    image = models.ImageField(verbose_name='Imagen', upload_to='services')
    published = models.DateTimeField(default=now, verbose_name='Fecha de publicacion') # auto_now -> cada vez que se ejecuta una instancia
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category,verbose_name='Categories', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion') # auto_now_add -> al crearse
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion') # auto_now -> cada vez que se ejecuta una instancia

    def __str__(self):
        return self.title