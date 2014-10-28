# -*- encoding: utf-8 -*-
import hashlib, datetime, random
from django.utils import timezone
from rest_framework import viewsets
from forms import *
from .forms import CrearUser
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,render_to_response, get_object_or_404
from app.serializers import LibrosSerializer, UserSerializer, NotasSerializer, LectorSerializer
from django.template.context import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
import time

# Create your views here.

def home(request):
    sobreMi = SobreMi.objects.all()
    libros = Libros.objects.order_by("-tymestamp").all()
    notas = Notas.objects.order_by("-tymestamp").all()
    lectores = Lector.objects.order_by("-votos").all()
    template = "index.html"
    time.sleep(3)
    #form = AutenticarPorEmail(request.POST or None)
    form = AuthenticationForm(data=request.POST or None)

    if form.is_valid():
        login(request, form.get_user())
        return HttpResponseRedirect("/#reader")

    # return render_to_response(template,context_instance = RequestContext(request,locals()))
    return render(request,template,locals())

def loveE(request,id_notas):
    nota = get_object_or_404(Notas, pk = id_notas)

    nota.votos = nota.votos + 1
    nota.save()

    return HttpResponse("/#notes")

@login_required
def loveL(request,id_lector):
    lector = get_object_or_404(Lector, pk = id_lector)

    lector.votos = lector.votos + 1
    lector.save()

    return HttpResponseRedirect("/#reader")

@login_required
def add(request):
    if request.POST:
        form = LectorForm(request.POST)
        if form.is_valid():
            lector = form.save(commit = False)
            lector.usuario = request.user
            lector.save()
            return HttpResponseRedirect("/#reader")
    else:
        form = LectorForm()
    template = "form.html"
    return render_to_response(template,context_instance = RequestContext(request,locals()))


def singup(request):
    form = CrearUser(request.POST or None)

    if form.is_valid():
        form.save()
        # login new user
        # formLogin = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        # login(request, formLogin)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        activation_key = hashlib.sha1(str(random.random())).hexdigest()[:40]
        key_expires = datetime.datetime.today() + datetime.timedelta(2)

        user = User.objects.get(username = username)

        new_profile = UserProfile(user =user, activation_key = activation_key, key_expires = key_expires)
        new_profile.save()

        # enviar correo de activacion
        email_subject = 'Confirmación de cuenta'
        email_body = "Hola %s. \nGracias por registrarte. Para activar tu cuenta, haz click en el link que te facilitamos antes de 48 horas. \nhttp://localhost:8000/confirm/%s" % (username, activation_key)

        send_mail(email_subject,email_body,'jorgechato1@gmail.com',[email], fail_silently = False)
        return HttpResponseRedirect("/register_success")

    return render(request,'singup.html',{'form':form})

def register_confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(UserProfile , activation_key = activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.user
    user.is_active = True
    user.save()

    return render_to_response('confirm.html')

#crear api
class LibrosViewSet(viewsets.ModelViewSet):
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NotasViewSet(viewsets.ModelViewSet):
    queryset = Notas.objects.all()
    serializer_class = NotasSerializer

class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer

