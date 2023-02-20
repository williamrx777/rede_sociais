from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensagem

@login_required
def enviar_mensagem(request, destinatario_id):
    destinatario = get_object_or_404(User, id=destinatario_id)
    if request.user == destinatario:
        return redirect('perfil')
    # verificar se o destinatário é um amigo do usuário, etc.
    if request.method == 'POST':
        texto = request.POST.get('texto')
        mensagem = Mensagem(remetente=request.user, destinatario=destinatario, texto=texto)
        mensagem.save()

    return render(request, 'enviar_mensagem.html', {'destinatario': destinatario})

@login_required
def exibir_conversa(request, destinatario_id):
    destinatario = get_object_or_404(User, id=destinatario_id)
    mensagens = Mensagem.objects.filter(remetente=request.user, destinatario=destinatario) | Mensagem.objects.filter(remetente=destinatario, destinatario=request.user)
    mensagens = mensagens.order_by('data_hora')
    return render(request, 'exibir_conversa.html', {'destinatario': destinatario, 'mensagens': mensagens})
