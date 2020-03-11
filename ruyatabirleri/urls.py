from django.urls import path
from .import views

app_name = "ruyatabirleri"

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('tefeul', views.tefeul, name='tefeul'),
    path('tefeul/tefeul_nedir', views.tefeul_nedir, name='tefeul_nedir'),
    path('tefeul/tefeul_yap', views.tefeul_yap, name='tefeul_yap'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('ruyatabirleri_gizlilik/', views.gizlilik, name='gizlilik'),
    path('yildizname/', views.yildizname, name='yildizname'),
    path('yidizname/yildizname_nedir/', views.yildizname_nedir, name='yildizname_nedir'),
    path('ruyatabirleri/', views.ruyatabirleri, name='ruyatabirleri'),
    path('ruyatabirleri/ruyatabirleri_nedir/', views.ruyatabirleri_nedir, name='ruyatabirleri_nedir'),
    path('ruyatabirleri/ruyada-<slug:slug>-gormek/q1w2e3r4t5y6u7', views.ruyatabirleri_ayrinti, name='ruyatabirleri_ayrinti'),
    path('ruyatabirleri/ruyada-<slug:slug>-gormek/q1w2e3r4t5y6u7', views.ruyatabirleri_ayrinti, name='my_comment_was_posted'),
    path('<str:harf>/q1w2e3r4t5y6u7', views.harf_sayfalari, name='harf_sayfalari'),
]
