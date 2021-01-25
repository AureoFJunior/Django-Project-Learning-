from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    html = f'<html><body>Agora é {now} </body></html>'
    return HttpResponse(html)

def home2(request):
    aa = 'vai se fuder mano'
    #html2 = f'<html><body><h1>{aa}</h1></body></html>'
    return render(request, 'contas/home2.html')
