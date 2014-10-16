from django.contrib.auth.models import User

__author__ = 'jorge'
from rest_framework import serializers
from models import Libros, Notas, Lector


class LibrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Libros
        fields = ('titulo','sinopsis','imagen','url',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = User
        fields = ('url','username','email',)

class NotasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Notas
        fields = ('url','titulo','comentario','votos','tymestamp',)

class LectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Lector
        fields = ('url','usuario','comentario','votos','tymestamp',)