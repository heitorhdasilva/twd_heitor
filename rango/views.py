from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    textp = """
    <h1>Olá heitor!</h1>
    <a href = '/rango/about'>About </a>
    """
    return HttpResponse(textp)

def about(request):
    texto = """
    <h1>Sobre o Rango</h1>
    <a href = '/rango'>Voltar</a>
    """
    return HttpResponse(texto)