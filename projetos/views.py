from django.shortcuts import render
from .models import Projeto

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos/listar_projetos.html', {'projetos': projetos})


