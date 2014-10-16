from django.contrib import admin
from models import *
from actions import export_as_csv

# Register your models here.
class LibrosAdmin(admin.ModelAdmin):
    list_display = ('titulo','sinopsis','url','pintar_cover',)
    search_fields = ['titulo',]
    list_editable = ('titulo', 'sinopsis', 'url',)
    list_display_links = ('pintar_cover',)
    actions = [export_as_csv]

    def pintar_cover(self, obj):
        url = obj.mostrar_cover_en_admin()
        tag = '<img src="%s" alt="">' %url
        return tag
    pintar_cover.allow_tags = True


class NotasAdmin(admin.ModelAdmin):
    list_display = ('es_popular','titulo','tymestamp', 'pintar_love', )
    list_filter = ('tymestamp',)
    search_fields = ['titulo',]
    list_editable = ('titulo', )
    list_display_links = ('tymestamp',)
    actions = [export_as_csv]

    def pintar_love(self, obj):
        url = obj.mostrar_love_notas()
        tag = '<img src="%s" alt="">' %url
        return tag
    pintar_love.allow_tags = True
    pintar_love.admin_order_field = 'votos'

class LectorAdmin(admin.ModelAdmin):
    list_display = ('es_popular','usuario','tymestamp', 'pintar_love',)
    list_filter = ('usuario','tymestamp',)
    search_fields = ['usuario__username']
    list_display_links = ('usuario',)
    actions = [export_as_csv]
    raw_id_fields = ('usuario',)

    def pintar_love(self, obj):
        url = obj.mostrar_love_lector()
        tag = '<img src="%s" alt="">' %url
        return tag
    pintar_love.allow_tags = True
    pintar_love.admin_order_field = 'votos'

admin.site.register(SobreMi)
admin.site.register(Libros, LibrosAdmin)
admin.site.register(Notas, NotasAdmin)
admin.site.register(Lector, LectorAdmin)
