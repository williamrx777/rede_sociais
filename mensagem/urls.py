from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('chat/<int:destinatario_id>/', views.chat, name='chat'),

]
