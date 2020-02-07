from django.urls import path
from .import views

app_name = "ruyatabirleri"

urlpatterns = [
    path('', views.ruyatabirleri, name='ruyatabirleri'),
    path('ruyatabirleri/ruyada-<slug:slug>-gormek/q1w2e3r4t5y6u7', views.ruyatabirleri_ayrinti, name='ruyatabirleri_ayrinti'),
    path('ruyatabirleri/ruyada-<slug:slug>-gormek/q1w2e3r4t5y6u7', views.ruyatabirleri_ayrinti, name='my_comment_was_posted'),
    path('ruyatabirleri_ruya_nedir/', views.ruya_nedir, name='ruya_nedir'),
    path('ruyatabirleri_ruya_ile_amel/', views.ruya_ile_amel, name='ruya_ile_amel'),
    path('ruyatabirleri_ruya_hadis/', views.ruya_hadis, name='ruya_hadis'),
    path('ruyatabirleri_gizlilik/', views.gizlilik, name='gizlilik'),
    path('<str:harf>/q1w2e3r4t5y6u7', views.harf_sayfalari, name='harf_sayfalari'),
]
