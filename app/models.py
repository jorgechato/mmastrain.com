from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from server.settings import STATIC_URL


class SobreMi(models.Model):
    imagen = models.ImageField(upload_to = 'img')
    descripcion = models.CharField(max_length = 10000)
    descripcionFin = models.CharField(max_length = 10000)

class Libros(models.Model):
    titulo = models.CharField(max_length = 140)
    sinopsis = models.CharField(max_length = 900)
    imagen = models.ImageField(upload_to = 'img/covers')
    url = models.URLField()

    def __unicode__(self):
        return self.titulo

    def mostrar_cover_en_admin(self):
        #return "http://127.0.0.1:8000/ %s" % self.imagen
        return "http://placehold.it/166x250/000/fff&text=%s" % self.titulo

class Notas(models.Model):
    titulo = models.CharField(max_length = 140)
    comentario = models.CharField(max_length = 600)
    votos = models.IntegerField(default = 0)
    tymestamp = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.titulo

    def mostrar_love_notas(self):
        return "http://placehold.it/200x100/bb242a/fff&text=%i+love" % self.votos
    def es_popular(self):
        return self.votos > 10
    es_popular.boolean = True

class Lector(models.Model):
    usuario = models.ForeignKey(User)
    comentario = models.CharField(max_length = 140)
    votos = models.IntegerField(default = 0)
    tymestamp = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return unicode(self.usuario)

    def mostrar_love_lector(self):
        return "http://placehold.it/200x100/bb242a/fff&text=%i+love" % self.votos

    def es_popular(self):
        return self.votos > 10
    es_popular.boolean = True