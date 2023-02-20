from django.urls import path
from . import views

urlpatterns = [
    path('enviar_mensagem/<int:destinatario_id>/', views.enviar_mensagem, name='enviar_mensagem'),
    path('conversa/<int:destinatario_id>/', views.exibir_conversa, name='exibir_conversa'),
]
