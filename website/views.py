from django.shortcuts import render
from website.models import MensagemContacto

# Create your views here.

def homesite(request):
    return render(request, 'homesite.html')


def sobresite(request):
    return render(request, 'sobresite.html')

def passageiro(request):
    return render(request, 'passageiro.html')

def motoqueiro(request):
    return render(request, 'motoqueiro.html')

def sobresite(request):
    return render(request, 'sobresite.html')



from django.shortcuts import render, redirect
from .models import MensagemContacto
from django.contrib import messages


def mensagemcontacto(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cidade = request.POST.get('cidade')
        mensagem_texto = request.POST.get('mensagem')

        MensagemContacto.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            cidade=cidade,
            mensagem=mensagem_texto
        )

        messages.success(request, "Mensagem enviada com sucesso!")

        # REDIRECIONA PARA A MESMA PÁGINA
        return redirect('contacto')

    return render(request, 'contacto.html')

def servico(request):
    return render(request, 'servico.html')