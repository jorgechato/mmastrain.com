from django.conf.urls import patterns, include, url
from django.contrib.auth import views
from django.contrib import admin
from rest_framework import routers
from app.views import LibrosViewSet, UserViewSet, NotasViewSet, LectorViewSet

router = routers.DefaultRouter()
router.register(r'libros', LibrosViewSet)
router.register(r'user', UserViewSet)
router.register(r'notas', NotasViewSet)
router.register(r'lector', LectorViewSet)

urlpatterns = patterns('',
    url(r'^$', 'app.views.home', name='home'),
    url(r'^loveE/(\d+)$', 'app.views.loveE', name='loveE'),
    url(r'^loveL/(\d+)$', 'app.views.loveL', name='loveL'),
    url(r'^add/$', 'app.views.add', name='add'),
    url(r'^singup/', 'app.views.singup', name='singup'),

    url(r'^api/', include(router.urls),name = 'api'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^social/',include('social.apps.django_app.urls', namespace='social')),

    url(r'^logout/$', views.logout, name='logout'),
)
