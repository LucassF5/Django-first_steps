from django.contrib import admin

from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda') # Campos que serão exibidos na listagem
    list_display_links = ('id', 'nome') # Campos que serão links para a edição
    search_fields = ('nome',) # Campos que serão pesquisáveis

admin.site.register(Fotografia, ListandoFotografias)  # Campo para registrar o modelo no admin
