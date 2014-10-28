import datetime
from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import get_thumbnail

# Create your models here.
from server.settings import STATIC_URL


class SobreMi(models.Model):
    imagen = models.ImageField(upload_to = 'img')
    descripcion = models.TextField(max_length = 10000)
    descripcionFin = models.TextField(max_length = 10000, blank = True)

class Libros(models.Model):
    titulo = models.CharField(max_length = 140)
    sinopsis = models.TextField(max_length = 900)
    imagen = models.ImageField(upload_to = 'img/covers')
    link = models.URLField(blank = True)
    tymestamp = models.DateTimeField(auto_now_add = True)
    boton = models.CharField(max_length = 140, blank = True)

    def __unicode__(self):
        return self.titulo

    def mostrar_cover_en_admin(self):
        return get_thumbnail(self.imagen, '166x250').url
        # return "http://placehold.it/166x250/000/fff&text=%s" % self.titulo

class Notas(models.Model):
    titulo = models.CharField(max_length = 140)
    comentario = models.TextField(max_length = 600)
    votos = models.PositiveIntegerField(default = 0)
    tymestamp = models.DateTimeField(auto_now_add = True)
    imagen = models.ImageField(upload_to = 'img/notas')

    def __unicode__(self):
        return self.titulo

    def mostrar_love_notas(self):
        return "http://placehold.it/200x100/bb242a/fff&text=%i+love" % self.votos
    def es_popular(self):
        return self.votos > 10
    es_popular.boolean = True

class Lector(models.Model):
    usuario = models.ForeignKey(User)
    comentario = models.TextField(max_length = 140)
    votos = models.PositiveIntegerField(default = 0)
    tymestamp = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return unicode(self.usuario)

    def mostrar_love_lector(self):
        return "http://placehold.it/200x100/bb242a/fff&text=%i+love" % self.votos

    def es_popular(self):
        return self.votos > 10
    es_popular.boolean = True

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length = 40, blank = True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = u'User profiles'
"""
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.sessions.models import Session


@receiver(post_save)
def clear_cache(sender, **kwargs):
    if sender != Session:
        cache.clear()"""