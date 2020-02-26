from .forms import AramaForm, YildiznameForm, iletisimForm
from .models import Ruyatabirleri, ArananKelimeler
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

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

            tabir1 = Ruyatabirleri.objects.filter (kelime__startswith=n)

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

def ruyatabirleri_ayrinti (response, slug=None):
    tabir1 = get_object_or_404 (Ruyatabirleri, slug=slug)
    karakter_satiri=int(len (tabir1.tabiri)/100)
    sayac=0
    for i in tabir1.tabiri:
        if i == "\n":
            sayac +=1
    if len(tabir1.tabiri) > 100:
        satir=(sayac+karakter_satiri)
    else:
        satir=(sayac+2)
    object_pk=tabir1.id
    form = AramaForm ()
    return render (response, 'ruyatabirleri/ruyatabirleri_ayrinti.html', {'satir':satir,'tabir1': tabir1, 'form': form, 'object_pk': object_pk})

def harf_sayfalari (response, harf):
    tabir1 = Ruyatabirleri.objects.filter (kelime__startswith=harf)
    arama_sonuc_sayisi=len(tabir1)
    form = AramaForm ()
    return render(response,'ruyatabirleri/ruyatabirleri_sonuc.html', {'arama_sonuc_sayisi': arama_sonuc_sayisi, 'tabir1': tabir1, 'form': form})

def anasayfa (request):
    return render(request,'ruyatabirleri/anasayfa.html', {})

def yildizname (request):
    return render(request,'ruyatabirleri/yildizname.html', {})

def yildizname_nedir (request):
    return render(request,'ruyatabirleri/yildizname_nedir.html', {})

def ruyatabirleri_nedir (request):
    return render(request,'ruyatabirleri/ruyatabirleri_nedir.html', {})

def yildizname (response):
    if response.method == "POST":
        form = YildiznameForm(response.POST)
        if form.is_valid():
            cinsiyet= form.cleaned_data.get('cinsiyet')
            isim = form.cleaned_data.get('isim')
            anne_ismi = form.cleaned_data.get('anne_ismi')
            #--------girilen harfler küçük harfe dönüştürüldü.---------
            isim=isim.replace("I", "ı").replace("İ", "i").lower()
            anne_ismi=anne_ismi.replace("I", "ı").replace("İ", "i").lower()
            #--------------------------bitti------------------------------------
            #----Cinsiyet seçiminin yapılması ve isimler için doğru Karakter girilmesi sağlanacak yoksa hata verecek---
            if cinsiyet == "Cinsiyetiniz":
                mesaj = 'Lütfen Cinsiyet Seçimini Yapınız'
                form = YildiznameForm ()
                return render (response, 'ruyatabirleri/yildizname.html', {'mesaj': mesaj, 'form': form})
            else:
                pass
            sesli_harfler= 'aeıiuüoö'
            sessiz_harfler= 'bcçdfgğhjklmnprsştvyzwqx'
            harfler='bcçdfgğhjklmnprsştvyzaeıiuüo ö'
            if len(isim)<3 or len(anne_ismi)<3:
                mesaj = 'İsminiz veya anne isminiz çok kısa. Tekrar Deneyiniz.'
                form = YildiznameForm ()
                return render (response, 'ruyatabirleri/yildizname.html', {'mesaj': mesaj, 'form': form})
            else:
                pass
            for harf in isim:
                if not harf in harfler:
                    mesaj = 'İsminizde Türkçe Harfler Dışında Karakter Kullanmayınız.'
                    form = YildiznameForm ()
                    return render (response, 'ruyatabirleri/yildizname.html', {'mesaj': mesaj, 'form': form})
                else:
                    pass
            for harf in anne_ismi:
                if not harf in harfler:
                    mesaj = 'Anne İsminde Türkçe Harfler Dışında Karakter Kullanmayınız.'
                    form = YildiznameForm ()
                    return render (response, 'ruyatabirleri/yildizname.html', {'mesaj': mesaj, 'form': form})
                else:
                    pass
            #--------------------Karakter Kontrolü bitti----------------

            form.save () #karakterler doğru girilmişse db ye kaydediyoruz.

            #---------------birden fazla isim varsa tespit edilip tüm isimler bir dosyaya yazıldı-----------
            isimler=isim.strip().split(' ') #bir den fazla ismi varsa boşluktan bölerek her birini elde ediyoruz
            hesap_kutusu=[] # üç harften küçük kelimeleri eliyoruz kalanları buraya yazıyoruz
            for i in range (len(isimler)):
                if not len(isimler[i]) < 3:
                    hesap_kutusu +=[isimler[i]]

            anne_isimleri=anne_ismi.strip().split(' ')  #bir den fazla ismi varsa boşluktan bölerek her birini elde ediyoruz
            for i in range (len(anne_isimleri)):
                if not len(anne_isimleri[i]) < 3:
                    hesap_kutusu +=[anne_isimleri[i]]

            #---------------EBCED hesabı Yapılacak.------------------------
            harf_degerleri={'a':1, 'b':2, 'c':3, 'ç':3, 'd':4, 'e':1, 'f':8, 'g':8, 'ğ':4, 'h':5, 'ı':1, 'i':1,
                            'j':7, 'k':4, 'l':6, 'm':4, 'n':2, 'o':7, 'ö':7, 'p':2, 'r':8, 's':0, 'ş':0,
                            't':4, 'u':7, 'ü':7, 'v':6, 'y':10, 'z':7,}

            toplanacak_harfler=""
            harflerin_toplami=0

            for i in range(len(hesap_kutusu)):
                for z in range(len(hesap_kutusu[i])):
                    if hesap_kutusu[i][z] in sessiz_harfler:
                        toplanacak_harfler +=hesap_kutusu[i][z]

            for i in range(len(hesap_kutusu)):
                if hesap_kutusu[i][0] in sesli_harfler:
                    toplanacak_harfler +=hesap_kutusu[i][0]

            print(toplanacak_harfler)

            for i in toplanacak_harfler:
                harflerin_toplami +=harf_degerleri[i]
            print(harflerin_toplami)

            mod=(harflerin_toplami)%12
            print(mod)
            #-----------EBCED Hesabı Bitti. Mod Bulundu.---------------
            return render (response, 'ruyatabirleri/yildizname_sonuc.html', {'cinsiyet': cinsiyet, 'mod': mod})
        mesaj = 'Lütfen Formu Doldurunuz.'
        return render(response, 'ruyatabirleri/yildizname.html', {'form': form, 'mesaj': mesaj})
    else:
        form = YildiznameForm ()
        return render(response, 'ruyatabirleri/yildizname.html', {'form': form})


def iletisim (response):
    if response.method == "POST":
        form = iletisimForm(response.POST)
        if form.is_valid():
            isim = form.cleaned_data.get ('isim')
            print(isim)
            soy_isim = form.cleaned_data.get ('soy_isim')
            print(soy_isim)
            eposta = form.cleaned_data.get ('eposta')
            print(eposta)
            ileti = form.cleaned_data.get ('mesaj')
            print(ileti)
            #----Tüm kutucukların doldurulması sağlandı yoksa hata verecek---
            if len(isim)<1 or len(soy_isim)<1 or len(eposta)<1 or len(ileti)<1:
                mesaj = 'Kutucukları Doldurunuz.'
                form = iletisimForm ()
                return render (response, 'ruyatabirleri/iletisim.html', {'mesaj': mesaj, 'form': form})
            else:
                pass
            #--------------------kutu Kontrolü bitti----------------
            form.save()
            mesaj= "Gönderiniz başarıyla kaydedildi."
            form = iletisimForm ()
            return render(response, 'ruyatabirleri/iletisim.html', {'form': form, 'mesaj': mesaj})
        mesaj = 'Lütfen Formu Doldurunuz.'
        return render (response, 'ruyatabirleri/iletisim.html', {'form': form, 'mesaj': mesaj})
    else:
        form = iletisimForm ()
        return render(response, 'ruyatabirleri/iletisim.html', {'form': form})