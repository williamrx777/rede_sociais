from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensagem

@login_required
def chat(request, destinatario_id=None):
    destinatario = None
    mensagens = None

    if destinatario_id:
        destinatario = get_object_or_404(User, id=destinatario_id)

        if request.user == destinatario:
            return redirect('perfil')

        if request.method == 'POST':
            texto = request.POST.get('texto')
            mensagem = Mensagem(remetente=request.user, destinatario=destinatario, texto=texto)
            mensagem.save()

            # Redireciona para a mesma URL, mas sem o parâmetro do destinatário
            return redirect('chat')

        mensagens = Mensagem.objects.filter(remetente=request.user, destinatario=destinatario) | Mensagem.objects.filter(remetente=destinatario, destinatario=request.user)
        mensagens = mensagens.order_by('data_hora')

    return render(request, 'chat.html', {'destinatario': destinatario, 'mensagens': mensagens})
