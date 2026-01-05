from django.shortcuts import render

# Create your views here.

def homesite(request):
    return render(request, 'homesite.html')


def sobresite(request):
    return render(request, 'sobresite.html')

def passageiro(request):
    return render(request, 'passageiro.html')

def motoqueiro(request):
    return render(request, 'motoqueiro.html')