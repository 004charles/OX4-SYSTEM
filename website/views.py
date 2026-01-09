from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib import messages
from .models import MensagemContacto

# Tenta importar Servico, se não existir, define como None
try:
    from .models import Servico
    HAS_SERVICO_MODEL = True
except ImportError:
    Servico = None
    HAS_SERVICO_MODEL = False

# Create your views here.

def homesite(request):
    context = {}
    if HAS_SERVICO_MODEL:
        context['servicos'] = Servico.objects.filter(ativo=True).order_by('ordem')[:4]
    return render(request, 'homesite.html', context)

def sobresite(request):
    return render(request, 'sobresite.html')

def passageiro(request):
    return render(request, 'passageiro.html')

def motoqueiro(request):
    return render(request, 'motoqueiro.html')

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
    context = {}
    if HAS_SERVICO_MODEL:
        context['servicos'] = Servico.objects.filter(ativo=True).order_by('ordem')
    else:
        context['servicos'] = []
        context['error'] = "Modelo de Serviços não está configurado."
    
    return render(request, 'servico.html', context)

class ServicoDetailView(DetailView):
    template_name = 'detalhe_servico.html'
    context_object_name = 'servico'
    
    def get_queryset(self):
        if HAS_SERVICO_MODEL:
            return Servico.objects.all()
        return []
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if HAS_SERVICO_MODEL and self.object:
            servico = self.object
            outros_servicos = Servico.objects.filter(
                categoria=servico.categoria,
                ativo=True
            ).exclude(id=servico.id).order_by('ordem')[:5]
            context['outros_servicos'] = outros_servicos
        else:
            context['outros_servicos'] = []
        
        return context