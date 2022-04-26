from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse('Hello world')


def turma_view(request):
    nome = "Programação Web"
    return HttpResponse(f"Olá turma de {nome}")


def sauda_view(request, nome):
    return HttpResponse(f"Olá {nome.capitalize()}!")
