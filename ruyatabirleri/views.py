import random
from .forms import AramaForm, YildiznameForm, iletisimForm
from .models import Ruyatabirleri, KuranBilgi, KuranKelime, ArananKelimeler
from django.shortcuts import render, get_object_or_404

def ruyatabirleri (response):
    if response.method == "POST":
        form = AramaForm(response.POST)
        if form.is_valid():
            n1 = form.cleaned_data["kelime"]

            #------------girilen kelime küçük harflere dönüştürüldü----------
            n=n1.replace("I", "ı").replace("İ", "i").lower()
            #------------------------------------------------------

            #------------Karakter Kontrolü yapıldı. Uygun olmayan varsa hata verildi.-------------
            #sesli_harfler= 'aeıiuüoö'
            #sessiz_harfler= 'bcçdfgğhjklmnprsştvyzwqx'
            harfler='bcçdfgğhjklmnprsştvyzaeıiuüo ö'
            for harf in n:
                if not harf in harfler:
                    mesaj = ' : Sadece Türkçe Harflerden Oluşmalıdır.'
                    return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'n1': n1, 'mesaj': mesaj})
                else:
                    pass
            #--------------------Karakter Kontrolü bitti----------------
            ArananKelimeler.objects.create (kelime=n)  # aranan kelime kontrollerden sonra db kaydedildi.
            #-----------Aranan kelimenin tabiri db den alında yoksa hata verip en yakın tabir verildi---------
            tabir1 = Ruyatabirleri.objects.filter (kelime__contains=n)

            if tabir1:
                return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'tabir1': tabir1}) #tabir var
            else:
#--birden fazla kelime girilmiş ise tabiri de yoksa kelimeleri parçalayarak en yakın anlamaı bulma----
                kelimlere_ayir = n.split (" ")
                tabir_listesi=[]
                kelimlere_ayir2 = [i for i in kelimlere_ayir if i != 'rüyada' if i != 'görmek'
                                   if i != 'rüyamda' if i != 'ruyada' if i != 'ruyamda' if i != 'gördüm']
                for klm in kelimlere_ayir2:
                    tabir1 = Ruyatabirleri.objects.filter (kelime__contains=klm)
                    if not tabir1:
                        s=0
                        while not tabir1:
                            k=len(klm)
                            s +=1
                            k1=k-s
                            klm1=klm[:k1]
                            tabir1 = Ruyatabirleri.objects.filter (kelime__contains=klm1)
                        for i in tabir1:
                            tabir_listesi +=[i]
                    else:
                        for i in tabir1:
                            tabir_listesi += [i]
                tabir1=tabir_listesi
                mesaj = "Aradığınız rüya yorumu bulunamamıştır. En yakın yorumlar aşağıda listelenmişti."
                return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'mesaj': mesaj, 'tabir1': tabir1})
        else:
            pass
        form = AramaForm ()
        mesaj = 'Lütfen Bir Kelime Yazınız.'
        return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'mesaj': mesaj, 'form': form})
    else:
        form = AramaForm ()
        return render(response,'ruyatabirleri/ruyatabirleri_anasayfa.html', {'form':form})

def gizlilik (request):
    return render(request,'ruyatabirleri/anasayfa_gizlilik.html', {})

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
    form = AramaForm ()
    return render(response,'ruyatabirleri/ruyatabirleri_anasayfa.html', {'tabir1': tabir1, 'form': form})

def anasayfa (request):
    return render(request,'ruyatabirleri/anasayfa.html', {})

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
            soy_isim = form.cleaned_data.get ('soy_isim')
            eposta = form.cleaned_data.get ('eposta')
            ileti = form.cleaned_data.get ('mesaj')
            #----Tüm kutucukların doldurulması sağlandı yoksa hata verecek---
            if len(isim)<1 or len(soy_isim)<1 or len(eposta)<1 or len(ileti)<1:
                mesaj = 'Kutucukları Doldurunuz.'
                form = iletisimForm ()
                return render (response, 'ruyatabirleri/anasayfa_iletisim.html', {'mesaj': mesaj, 'form': form})
            else:
                pass
            #--------------------kutu Kontrolü bitti----------------
            form.save()
            mesaj= "Gönderiniz başarıyla kaydedildi."
            form = iletisimForm ()
            return render(response, 'ruyatabirleri/anasayfa_iletisim.html', {'form': form, 'mesaj': mesaj})
        mesaj = 'Lütfen Formu Doldurunuz.'
        return render (response, 'ruyatabirleri/anasayfa_iletisim.html', {'form': form, 'mesaj': mesaj})
    else:
        form = iletisimForm ()
        return render(response, 'ruyatabirleri/anasayfa_iletisim.html', {'form': form})

def tefeul (request):
    besmele = KuranBilgi.objects.get (id=1)  # besmele
    return render(request,'ruyatabirleri/tefeul.html', {'besmele': besmele})

def tefeul_yap (request):
    besmele = KuranBilgi.objects.get (id=1)  # besmele
    #hangi_sure = random.randint (1, 114)
    hangi_sure = 1
    bilgi_satiri = KuranBilgi.objects.filter (sure_no=hangi_sure)
    for item in bilgi_satiri:
        x1 = item.ayet_say
        hangi_ayet = random.randint (1, x1)
        bilgi_satiri_2 = KuranBilgi.objects.filter (sure_no=hangi_sure).filter (ayet_no=hangi_ayet)
        kelime_sayisi=KuranKelime.objects.filter (sure_no=hangi_sure).filter (ayet_no=hangi_ayet).count()
        hangi_kelime = random.randint (1, kelime_sayisi)
        bilgi_satiri_3 = KuranKelime.objects.filter (sure_no=hangi_sure).filter (ayet_no=hangi_ayet).filter (kelime_no=hangi_kelime)
        return render (request, 'ruyatabirleri/tefeul.html', {'besmele': besmele, 'bilgi_satiri_2': bilgi_satiri_2, 'hangi_kelime':hangi_kelime,
                                                              'bilgi_satiri_3':bilgi_satiri_3})

def tefeul_nedir (request):
    return render(request,'ruyatabirleri/tefeul_nedir.html', {})

def dua (request):
    return render(request,'ruyatabirleri/dua.html', {})

def dua_nedir (request):
    return render(request,'ruyatabirleri/dua_nedir.html', {})

def yasin (request):
    return render(request,'ruyatabirleri/dua_yasin.html', {})

def yasin_arapca (request):
    return render(request,'ruyatabirleri/dua_yasin_arapca.html', {})

def mubin (request):
    return render(request,'ruyatabirleri/dua_yasin_mubin.html', {})

def ayetelkursi (request):
    return render(request,'ruyatabirleri/dua_ayetelkursi.html', {})

def ayetelkursi_arapca (request):
    return render(request,'ruyatabirleri/dua_ayetelkursi_arapca.html', {})

def dua_ayet (request):
    return render(request,'ruyatabirleri/dua_dua_ayet.html', {})

def esmaul_husna (request):
    return render(request,'ruyatabirleri/dua_esmaul_husna.html', {})

def tefriciye (request):
    return render(request,'ruyatabirleri/dua_tefriciye.html', {})

def tefriciye_arapca (request):
    return render(request,'ruyatabirleri/dua_tefriciye_arapca.html', {})