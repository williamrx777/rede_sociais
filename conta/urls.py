from django.urls import path
from . import views

urlpatterns = [
    path ('',views.home,name='home'),
    path ('profile/', views.profile, name='profile'),
    path('remove_post/<int:id>', views.remove_post, name='remove_post'),
    path ('batepapo/', views.batepapo, name='batepapo'),
    path('remove_batepapo/<int:id>', views.remove_batepapo, name='remove_batepapo'),
]