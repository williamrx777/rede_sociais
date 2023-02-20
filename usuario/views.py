from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import  HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.messages import constants
from django.contrib import messages
# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos.')
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Digite duas senhas iguais.')
    try:
        user = User.objects.create_user(
            username=nome,
            email=email,
            password=senha,
        )
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso.')
        return redirect('logar')
    except:
        messages.add_message(request, constants.ERROR, 'Tente novamente.')
        return redirect('/usuario/cadastro/')


def logar(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome,password=senha)

        if user is not None:
            login(request, user)
            return redirect('/conta/')
        if request.user.is_authenticated:
            return redirect('/conta/')
        else:
            return HttpResponse('Erro usuario ou senha')

def sair(request):
    logout(request)
    return redirect('/usuario/logar/')