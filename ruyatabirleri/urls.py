from django.urls import path
from .import views
from django.utils.translation import gettext_lazy as _

app_name = "ruyatabirleri"

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path(_('dua/'), views.dua, name='dua'),
    path(_('dua-nedir/'), views.dua_nedir, name='dua_nedir'),
    path(_('dua/yasin'), views.yasin, name='yasin'),
    path(_('dua/yasin/mubin'), views.mubin, name='mubin'),
    path(_('dua/yasin/arapca'), views.yasin_arapca, name='yasin_arapca'),
    path(_('dua/ayetelkursi'), views.ayetelkursi, name='ayetelkursi'),
    path(_('dua/ayetelkursi/arapca'), views.ayetelkursi_arapca, name='ayetelkursi_arapca'),
    path(_('dua/dua_ayet'), views.dua_ayet, name='dua_ayet'),
    path(_('dua/esmaul_husna'), views.esmaul_husna, name='esmaul_husna'),
    path(_('dua/tefriciye'), views.tefriciye, name='tefriciye'),
    path(_('dua/tefriciye/arapca'), views.tefriciye_arapca, name='tefriciye_arapca'),
    path(_('tefeul/'), views.tefeul, name='tefeul'),
    path(_('tefeul-nedir/'), views.tefeul_nedir, name='tefeul_nedir'),
    path(_('tefeul/tefeul_yap'), views.tefeul_yap, name='tefeul_yap'),
    path(_('iletisim/'), views.iletisim, name='iletisim'),
    path(_('gizlilik/'), views.gizlilik, name='gizlilik'),
    path(_('yildizname/'), views.yildizname, name='yildizname'),
    path(_('yildizname-nedir/'), views.yildizname_nedir, name='yildizname_nedir'),
    path(_('ruyatabirleri/'), views.ruyatabirleri, name='ruyatabirleri'),
    path(_('ruyatabirleri-nedir/'), views.ruyatabirleri_nedir, name='ruyatabirleri_nedir'),
    path('ruyatabirleri/ruyada-<slug:slug>-gormek/q1w2e3r4t5y6u7', views.ruyatabirleri_ayrinti, name='ruyatabirleri_ayrinti'),
    path('ruyatabirleri/ruyada-<slug:slug>-gormek/q1w2e3r4t5y6u7', views.ruyatabirleri_ayrinti, name='my_comment_was_posted'),
    path('<str:harf>/q1w2e3r4t5y6u7', views.harf_sayfalari, name='harf_sayfalari'),
    path('<slug:slug>', views.ruyatabirleri_ayrinti_sbt_syf, name='ruyatabirleri_ayrinti_sbt_syf'),
]
