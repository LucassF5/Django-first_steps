from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by('-id').filter(publicada=True) 
    # Vai buscar todas as fotos que estão publicadas
    # O método order_by('-id') vai buscar as fotos na ordem decrescente de id
    
    return render(request, "galeria/index.html", {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) #pk = primary key
    # Vai receber o id da foto e buscar a foto no banco de dados
    # Caso não encontre, retorna um erro 404
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})