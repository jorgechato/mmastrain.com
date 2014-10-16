from django.http import HttpResponse, HttpResponseRedirect
# from datetime import datetime
from django.shortcuts import render,render_to_response, get_object_or_404
from rest_framework import viewsets
from app.serializers import LibrosSerializer, UserSerializer, NotasSerializer, LectorSerializer
# from models import *
from forms import *
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login


# Create your views here.

def home(request):
    sobreMi = SobreMi.objects.all()
    libros = Libros.objects.all()
    notas = Notas.objects.all()
    lectores = Lector.objects.order_by("-votos").all()
    template = "index.html"

    return render_to_response(template,locals())

def loveE(request,id_notas):
    nota = get_object_or_404(Notas, pk = id_notas)

    nota.votos = nota.votos + 1
    nota.save()

    return HttpResponseRedirect("/#notes")

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

#crear apide libros

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