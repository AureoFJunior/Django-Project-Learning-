from builtins import filter

from django.shortcuts import render
from django.http import HttpResponse
from .models import Transacao
from .forms import TransacaoForm
import datetime

def home(request):
    now = datetime.datetime.now()
    html = f'<html><body>Agora é {now} </body></html>'
    return HttpResponse(html)

def home2(request):
    aa = 'hello'
    data1 = {}
    data1['transacoes'] = ['t1', 't2', 't3']
    #html2 = f'<html><body><h1>{aa}</h1></body></html>'
    return render(request, 'contas/home2.html')

def listagem(request):
    data3 = {}
    data3['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data3)

def nova_transacao(request):
    forms = TransacaoForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return listagem(request)
    return render(request, 'contas/form.html', {'form': forms})

def update(request, pk):
    newtransacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=newtransacao)

    if form.is_valid():
        form.save()
        return listagem(request)

    return render(request, 'contas/form.html', {'form': form})