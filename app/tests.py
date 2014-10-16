from django.test import TestCase
from .models import Notas, Lector, Libros
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your tests here.
class SimpleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = 'jorge', password = 'prueba1234')


    def test_es_popular_nota(self):
        # si una nota tiene menos de 11 lovs no es popular

        nota = Notas.objects.create(titulo = 'prueba',comentario = 'esto es una prueba',
                                    votos = 0)

        self.assertEquals(nota.votos, 0)
        self.assertEquals(nota.es_popular(), False)

        # si una nota tiene mas de 10 lovs es popular
        nota.votos = 69876
        nota.save()
        self.assertEquals(nota.votos, 69876)
        self.assertEquals(nota.es_popular(), True)

    def test_es_popular_Lector(self):
        # si una nota tiene menos de 11 lovs no es popular

        lector = Lector.objects.create(usuario = self.user,comentario = 'esto es una prueba',
                                       votos = 0)

        self.assertEquals(lector.votos, 0)
        self.assertEquals(lector.es_popular(), False)

        # si una nota tiene mas de 10 lovs es popular
        lector.votos = 69876
        lector.save()
        self.assertEquals(lector.votos, 69876)
        self.assertEquals(lector.es_popular(), True)

    def test_views(self):
        res = self.client.get(reverse('home'))
        self.assertEquals(res.status_code,200)

        #res = self.client.get(reverse('loveE'))
        #self.assertEquals(res.status_code,200)

        self.client.login(username = 'jorge', password = 'prueba1234')

        #res = self.client.get(reverse('loveL'))
        #self.assertEquals(res.status_code,200)

        res = self.client.get(reverse('add'))
        self.assertEquals(res.status_code,200)

    def test_add(self):
        self.client.login(username = 'jorge', password = 'prueba1234')

        self.assertEquals(Lector.objects.count(), 0)
        data = {}
        data ['comentario'] = 'comentario de prueba'

        res = self.client.post(reverse('add'), data)
        self.assertEquals(res.status_code, 302)
        self.assertEquals(Lector.objects.count(), 1)

        lector = Lector.objects.all()[0]
        self.assertEquals(lector.comentario, data ['comentario'])