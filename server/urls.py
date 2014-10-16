from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from app.views import LibrosViewSet, UserViewSet, NotasViewSet, LectorViewSet

router = routers.DefaultRouter()
router.register(r'libros', LibrosViewSet)
router.register(r'user', UserViewSet)
router.register(r'notas', NotasViewSet)
router.register(r'lector', LectorViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^loveE/(\d+)$', 'app.views.loveE', name='loveE'),
    url(r'^loveL/(\d+)$', 'app.views.loveL', name='loveL'),
    url(r'^add/$', 'app.views.add', name='add'),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^logout/$', 'django.contrib.auth.logout', name='logout'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
