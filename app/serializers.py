from django.contrib.auth.models import User

__author__ = 'jorge'
from rest_framework import serializers
from models import Libros, Notas, Lector
# serializer para administrar el api

class LibrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Libros
        fields = ('url','titulo','sinopsis','imagen','link',)

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