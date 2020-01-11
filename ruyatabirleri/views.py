from .forms import AramaForm
from django.http import Http404, HttpResponseRedirect
from .models import Ruyatabirleri, ArananKelimeler
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

def ruyatabirleri (response):
    if response.method == "POST":
        form = AramaForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["kelime"]
            #------------girilen kelime küçük harflere dönüştürüldü----------
            n=n.replace("I", "ı").replace("İ", "i").lower()
            #------------------------------------------------------

            #------------Karakter Kontrolü yapıldı. Uygun olmayan varsa hata verildi.-------------
            sesli_harfler= 'aeıiuüoö'
            sessiz_harfler= 'bcçdfgğhjklmnprsştvyzwqx'
            harfler='bcçdfgğhjklmnprsştvyzwqxaeıiuüoö '
            for harf in n:
                if not harf in harfler:
                    mesaj = 'Lütfen Yazdığınız Harfleri Kontrol Ediniz ve Tekrar Deneyiniz.'
                    form = AramaForm ()
                    return render (response, 'ruyatabirleri/ruyatabirleri_sonuc_hata.html', {'mesaj': mesaj, 'form':form})
                else:
                    pass
            #--------------------Karakter Kontrolü bitti----------------

            tabir1 = Ruyatabirleri.objects.filter (kelime=n)

            arama_sonuc_sayisi=len(tabir1)

            #----Aranan Kelime db de varsa En çok Aranan Kelimelere girmesi için onay veriyoruz----
            if tabir1:
                ArananKelimeler.objects.create (kelime=n, uygunluk_onayi=True)  # aranan kelime kontrollerden sonra Uygun olarak db kaydedildi.
            else:
                ArananKelimeler.objects.create (kelime=n) #aranan kelime kontrollerden sonra db kaydedildi.

            #-----------Aranan kelime db tabloda yoksa verilecek uyarı------------
            if not tabir1:
                mesaj="Aradığınız Rüya Yorumu Bulunamamıştır. Lütfen Farklı Kelimeler ile Deneyiniz. "
                form = AramaForm ()
                return render (response, 'ruyatabirleri/ruyatabirleri_sonuc_hata.html', {'mesaj': mesaj, 'form': form})
            #-----------------------------------------------------------------------------
            else:
                form = AramaForm ()
                return render (response, 'ruyatabirleri/ruyatabirleri_sonuc.html', {'arama_sonuc_sayisi':arama_sonuc_sayisi, 'tabir1':tabir1, 'form':form})

        return HttpResponseRedirect ("/ruyatabirleri/")
    else:
        form = AramaForm ()

        #------En çok aranan kelimenin bulunması

        kutu=[]#aranan kelimeler kaydediliyor her kelime bir kez kaydediliyor
        kelimeler_aranan_anasayfa=ArananKelimeler.objects.all() #Aranan kelimelerin hepsini alıyoruz
        for i in kelimeler_aranan_anasayfa:
            if not i.kelime in kutu:
                kutu +=[i.kelime]
        #aranan kelimelerin onaylı olanlarının keç kere arandığını hesaplayıp ana tabloyu güncelliyoruz
        for i1 in kutu:
            arama_sayisi=ArananKelimeler.objects.filter(kelime=i1, uygunluk_onayi=True).count()
            Ruyatabirleri.objects.filter(kelime=i1).update(aranma_sayisi=arama_sayisi)

        son_liste = Ruyatabirleri.objects.all ().order_by ('-aranma_sayisi')[:10]
        #----------------------------------------------------

        son_eklenen_kelimeler = Ruyatabirleri.objects.all ().order_by('-ekleme_tarihi')[:10]

        return render(response,'ruyatabirleri/ruyatabirleri_anasayfa.html', {'form':form, 'son_liste': son_liste,
                                                                    'son_eklenen_kelimeler': son_eklenen_kelimeler })


def ruya_ile_amel (request):
    return render(request,'ruyatabirleri/ruyatabirleri_ruya_ile_amel.html', {})

def gizlilik (request):
    return render(request,'ruyatabirleri/ruyatabirleri_gizlilik.html', {})

#@login_required
def ruya_nedir (request):
    return render(request,'ruyatabirleri/ruyatabirleri_ruya_nedir.html', {})

def ruya_hadis (request):
    return render(request,'ruyatabirleri/ruyatabirleri_ruya_hadis.html', {})

def ruyatabirleri_ayrinti (response, kelime):
    tabir1 = get_object_or_404 (Ruyatabirleri, kelime=kelime)
    object_pk=tabir1.id
    form = AramaForm ()
    return render (response, 'ruyatabirleri/ruyatabirleri_ayrinti.html', {'tabir1': tabir1, 'form': form, 'object_pk': object_pk})

def harf_sayfalari (response, harf):
    tabir1 = Ruyatabirleri.objects.filter (kelime__startswith=harf)
    arama_sonuc_sayisi=len(tabir1)
    form = AramaForm ()
    return render(response,'ruyatabirleri/ruyatabirleri_sonuc.html', {'arama_sonuc_sayisi': arama_sonuc_sayisi, 'tabir1': tabir1, 'form': form})