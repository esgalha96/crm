from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import decorators
from .models import Ocorrencia
from .forms import OcorrenciaForm, MovimentacaoFormSet

@decorators.login_required()
def home(request):
    user = request.user
    ocorrencias = Ocorrencia.objects.prefetch_related('movimentacoes').filter(operador_responsavel = user)
    context = {
        'ocorrencias': ocorrencias
    }

    return render(request, "home.html", context=context)

@decorators.login_required()
def add_ocorrencia(request):
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, user=request.user)
        formset = MovimentacaoFormSet(request.POST, user=request.user)
        if form.is_valid() and formset.is_valid():
            ocorrencia = form.save()
            movimentacoes = formset.save(commit=False)
            for movimentacao in movimentacoes:
                movimentacao.ocorrencia = ocorrencia
                movimentacao.save()
            return redirect('home')
    else:
        form = OcorrenciaForm(user=request.user)
        formset = MovimentacaoFormSet(user=request.user)
    
    return render(request, 'add-ocorrencia.html', {'form': form, 'formset': formset})
