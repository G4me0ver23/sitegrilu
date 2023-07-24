from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from django.http import HttpResponse
from .models import Palavra

# Create your views here.
def index(request):
    palavras=Palavra.objects.all()
    return render(request,'lista/index.html',{'palavras':palavras})

def infos(request, palavra_id):
    palavra=get_object_or_404(Palavra, pk=palavra_id)
    if not palavra.informacao_set.exists():
        return render(request, 'lista/infos.html',{
            'palavra':palavra,
            'obs':'Palavra sem opções'
        })
    return render(request, 'lista/infos.html',{
        'palavra':palavra,
        'obs':''
    })