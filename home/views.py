from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def acerca(request):
    return render(request, 'home/acerca.html')

def contacto(request):
    return render(request, 'home/contacto.html')
