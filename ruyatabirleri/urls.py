from django.urls import path
from .import views

app_name = "ruyatabirleri"

urlpatterns = [
    path('', views.ruyatabirleri, name='ruyatabirleri'),
    path('ruyatabirleri_ruya_nedir/', views.ruya_nedir, name='ruya_nedir'),
    path('ruyatabirleri_ruya_ile_amel/', views.ruya_ile_amel, name='ruya_ile_amel'),
    path('ruyatabirleri_ruya_hadis/', views.ruya_hadis, name='ruya_hadis'),
    path('ruyatabirleri_gizlilik/', views.gizlilik, name='gizlilik'),
    path('<str:kelime>/', views.ruyatabirleri_ayrinti, name='ruyatabirleri_ayrinti'),
    path('<str:kelime>/', views.ruyatabirleri_ayrinti, name='my_comment_was_posted'),
]