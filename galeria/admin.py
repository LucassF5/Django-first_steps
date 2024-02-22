from django.contrib import admin

from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada') # Campos que serão exibidos na listagem
    list_display_links = ('id', 'nome') # Campos que serão links para a edição
    search_fields = ('nome',) # Campos que serão pesquisáveis
    list_filter = ["categoria"] # Campos que terão filtro
    list_editable = ['publicada'] # Campos que podem ser editados diretamente na listagem
    list_per_page = 10 # Quantidade de itens por página
    

admin.site.register(Fotografia, ListandoFotografias)  # Campo para registrar o modelo no admin
