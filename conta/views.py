from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Conta,Profile
from .models import Batepapo
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.
@login_required
def home(request):
    if request.method == "GET":
            texto = request.GET.get('texto')
            conta = Conta.objects.all()
            if texto:
                conta = Conta.objects.filter(texto__icontains=texto)
            else:
                conta
            return render(request, 'home.html', {'conta': conta,'texto':texto})
            print(conta)

    elif request.method == "POST":
        texto = request.POST.get('texto')
        foto = request.FILES.get('foto')

        conta = Conta(
            usuario=request.user,
            texto=texto,
            foto=foto,
        )
        conta.save()
        print(conta)
        messages.add_message(request, constants.SUCCESS, 'Adicionado com sucesso no feed.')
        return redirect('/conta/')
@login_required
def profile(request):
    if request.method == "GET":
        texto = request.GET.get('texto')
        conta = Conta.objects.filter(usuario=request.user)
        profile = Profile.objects.filter(usuario=request.user)
        if texto:
            conta = Conta.objects.filter(texto__icontains=texto)

        return render(request,'profile.html', {'conta':conta,'texto':texto,'profile':profile})
    elif request.method == "POST":
        perfil = request.FILES.get('perfil')
        capa = request.FILES.get('capa')
        profile = Profile(
            usuario=request.user,
            perfil=perfil,
            capa=capa,
        )
        print(profile)
        profile.save()
        messages.add_message(request, constants.SUCCESS, 'Adicionado com sucesso.')
        return redirect('/conta/profile/')

def remove_post(request, id):
    conta = Conta.objects.get(id=id)

    if not conta.usuario == request.user:
        return redirect('/conta/profile')

    conta.delete()
    messages.add_message(request, constants.SUCCESS, 'Removido com sucesso.')
    return redirect('/conta/profile')
@login_required
def batepapo(request):
    if request.method == "GET":
        mensagem = Batepapo.objects.all()
        return render(request, 'batepapo.html',{'mensagem':mensagem})
    elif request.method == "POST":
        imagem = request.FILES.get('imagem')
        mensagem = request.POST.get('mensagem')

        mensagem = Batepapo(
            usuario=request.user,
            imagem=imagem,
            mensagem=mensagem
        )
        mensagem.save()
        print(mensagem)
        messages.add_message(request, constants.SUCCESS, 'Enviado com sucesso.')
        return redirect('/conta/batepapo/')

def remove_batepapo(request, id):
    conta = Batepapo.objects.get(id=id)

    if not conta.usuario == request.user:
        return redirect('/conta/batepapo')

    conta.delete()
    messages.add_message(request, constants.SUCCESS, 'Removido com sucesso.')
    return redirect('/conta/batepapo')