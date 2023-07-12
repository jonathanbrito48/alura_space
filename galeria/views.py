from django.shortcuts import render


def index(request):

    dados = {
    1: {"Nome": "Nebulosa de Carina",
        "Legenda":"Webbtelescope.org / NASA / James Webb"},
    2: {"Nome": "Galaxia NGC 1079",
        "Legenda": "nasa.org / NASA / Hubble"}
}        
    return render(request, 'galeria/index.html',{"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')