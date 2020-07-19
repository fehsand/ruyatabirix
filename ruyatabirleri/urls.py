from django.urls import path
from .import views
from django.utils.translation import gettext_lazy as _

app_name = "ruyatabirleri"

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path(_('ruyatabiri-dua/'), views.dua, name='dua'),
    path(_('ruyatabiri-dua-nedir/'), views.dua_nedir, name='dua_nedir'),
    path(_('ruyatabiri-tefeul/'), views.tefeul, name='tefeul'),
    path(_('ruyatabiri-tefeul-nedir/'), views.tefeul_nedir, name='tefeul_nedir'),
    path(_('tefeul/tefeul_yap/'), views.tefeul_yap, name='tefeul_yap'),
    path(_('ruyatabiri-iletisim/'), views.iletisim, name='iletisim'),
    path(_('ruyatabiri-gizlilik/'), views.gizlilik, name='gizlilik'),
    path(_('ruyatabiri-yildizname/'), views.yildizname, name='yildizname'),
    path(_('ruyatabiri-yildizname-nedir/'), views.yildizname_nedir, name='yildizname_nedir'),
    path(_('ruyatabiri-ruyatabirleri/'), views.ruyatabirleri, name='ruyatabirleri'),
    path(_('ruyatabiri-ruyatabirleri-nedir/'), views.ruyatabirleri_nedir, name='ruyatabirleri_nedir'),
    path(_('ruyatabiri-ruya-yorumlatmak/'), views.rtx_yorum, name='rtx_yorum'),
    path(_('ruyatabiri-yonetici/'), views.yonetici, name='yonetici'),
    path(_('ruyatabirleri/'), views.rtx_ara_yorum, name='rtx_ara_yorum'),
    path(_('ruyatabirleri/ruyada-'+'<slug:slug>'+'-gormek/q1w2e3r4t5y6u7'), views.ruyatabirleri_ayrinti, name='ruyatabirleri_ayrinti'),
    path('ruyatabirleri/ruyada-<slug:slug>-gormek/q1w2e3r4t5y6u7', views.ruyatabirleri_ayrinti, name='my_comment_was_posted'),
    path('<str:harf>/q1w2e3r4t5y6u7', views.harf_sayfalari, name='harf_sayfalari'),
    path('ruyatabiri-<slug:slug>/', views.ruyatabirleri_ayrinti_sbt_syf, name='ruyatabirleri_ayrinti_sbt_syf'),


]