__author__ = 'jorge'

from django import forms
from django.forms import ModelForm
from models import *

class LectorForm(ModelForm):
    class Meta:
        model = Lector
        exclude = ("votos","usuario",)