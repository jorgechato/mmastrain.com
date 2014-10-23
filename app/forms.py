__author__ = 'jorge'

from django import forms
from models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class LectorForm(ModelForm):
    class Meta:
        model = Lector
        exclude = ("votos","usuario",)

class CrearUser(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email')
    # TODO validar con el email
    # def clean_email(self):


class AutenticarPorEmail(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)

    def __init__(self, *args,**kwargs):
        self.user_cache = None
        super(AutenticarPorEmail,self).__init__(*args,**kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        self.user_cache = authenticate(email=email,password=password)

        if self.user_cache is None:
            raise forms.ValidationError('Usuario incorrecto')
        elif not self.user_cache.is_active:
            raise forms.ValidationError('Usuario sin validar, revisa tu correo')

        return self.cleaned_data

    def get_user(self):
        return self.user_cache