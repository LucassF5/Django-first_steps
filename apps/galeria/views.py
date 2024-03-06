from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect("login")
    
    fotografias = Fotografia.objects.order_by('-id').filter(publicada=True)
    # Vai buscar todas as fotos que estão publicadas
    # O método order_by('-id') vai buscar as fotos na ordem decrescente de id

    return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)  # pk = primary key
    # Vai receber o id da foto e buscar a foto no banco de dados
    # Caso não encontre, retorna um erro 404
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect("login")
    fotografias = Fotografia.objects.order_by('-id').filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
            # Vai buscar as fotos que contém o nome digitado na barra de busca

    return render(request, "galeria/buscar.html", {"cards": fotografias})
