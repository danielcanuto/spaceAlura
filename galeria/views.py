from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia

from django.contrib import messages

def faca_login(request):
    return messages.error(request,"faça seu login")

def index(request):

    if not request.user.is_authenticated:
        faca_login(request)
        return redirect('login') 
    # fotografias = Fotografia.objects.all()
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicado=True)
    return render(request, 'galeria/index.html', {'cards':fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia":fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        faca_login(request)
        return redirect('login') 
    busca = Fotografia.objects.order_by('-data_fotografia').filter(publicado=True)
    

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            busca = busca.filter(nome__icontains=nome_a_buscar)
    return render(request, "galeria/buscar.html", {"cards": busca})
