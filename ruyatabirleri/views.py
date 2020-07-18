import random
from .forms import AramaForm, YildiznameForm, RtxiletisimForm, RTXYorumForm
from .models import Ruyatabirleri, KuranBilgi, KuranKelime, ArananKelimeler, Ruyatabirlerix_sbt, Ruyatabirlerix3, Rtx_iletisim, RTXyorum
from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language, gettext_lazy as _


def ruyatabirleri(response):
    # ---------------ingilizce----------------------
    if get_language () == 'en':
        if response.method == "POST":
            form = AramaForm (response.POST)
            if form.is_valid ():
                n1 = form.cleaned_data["kelime"]
                n = n1.lower ()  # girilen kelime küçük harflere dönüştürüldü
                # ------------Karakter Kontrolü yapıldı. Uygun olmayan varsa hata verildi.-------------
                harfler = 'abcdefghijklmnopqrstuvwxy z'
                for harf in n:
                    if not harf in harfler:
                        mesaj = ' : Please, Use Only English Letters.'
                        return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'n1': n1, 'mesaj': mesaj})
                    else:
                        pass
                # --------------------Karakter Kontrolü bitti----------------
                ArananKelimeler.objects.create (kelime=n)  # aranan kelime kontrollerden sonra db kaydedildi.
                # -----------Aranan kelimenin tabiri db den alında yoksa hata verip en yakın tabir verildi---------
                tabir1 = Ruyatabirlerix3.objects.filter (kelime_en__contains=n)
                if tabir1:
                    return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'tabir1': tabir1}) # tabir var
                else:
                    # --birden fazla kelime girilmiş ise tabiri de yoksa kelimeleri parçalayarak en yakın anlamaı bulma----
                    kelimlere_ayir = n.split (" ")
                    tabir_listesi = []
                    kelimlere_ayir2 = [i for i in kelimlere_ayir if i != 'dream' if i != 'dreamt' if i != 'seeing' if
                                       i != 'i' if i != 'my' if i != 'have']
                    for klm in kelimlere_ayir2:
                        tabir1 = Ruyatabirlerix3.objects.filter (kelime_en__contains=klm)
                        if not tabir1:
                            s = 0
                            while not tabir1:
                                k = len (klm)
                                s += 1
                                k1 = k - s
                                klm1 = klm[:k1]
                                tabir1 = Ruyatabirlerix3.objects.filter (kelime_en__contains=klm1)
                            for i in tabir1:
                                tabir_listesi += [i]
                        else:
                            for i in tabir1:
                                tabir_listesi += [i]
                    tabir1 = tabir_listesi
                    mesaj = "Unfortunately, The dream interpretation you are looking for has not been found. Other related dream interpretations were listed below."
                    return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'mesaj': mesaj, 'tabir1': tabir1})
            else:
                pass
            form = AramaForm ()
            mesaj = "Please, Write any keywords."
            return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'mesaj': mesaj, 'form': form})
        else:
            form = AramaForm ()
            return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'form': form})
    # ----------ispanyolca------
    elif get_language () == 'es':
        if response.method == "POST":
            form = AramaForm (response.POST)
            if form.is_valid ():
                n1 = form.cleaned_data["kelime"]
                n = n1.lower ()  # girilen kelime küçük harflere dönüştürüldü
                # ------------Karakter Kontrolü yapıldı. Uygun olmayan varsa hata verildi.-------------
                harfler = 'abcdefghijklmnñopqrstuvwxyàèòìùáéóíú z'
                for harf in n:
                    if not harf in harfler:
                        mesaj = ' : Por favor, use solo letras del alfabeto español.'
                        return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'n1': n1, 'mesaj': mesaj})
                    else:
                        pass
                # --------------------Karakter Kontrolü bitti----------------
                ArananKelimeler.objects.create (kelime=n)  # aranan kelime kontrollerden sonra db kaydedildi.
                # -----------Aranan kelimenin tabiri db den alında yoksa hata verip en yakın tabir verildi---------
                tabir1 = Ruyatabirlerix3.objects.filter (kelime_es__contains=n)
                if tabir1:
                    return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'tabir1': tabir1})  # tabir var
                else:
                    # --birden fazla kelime girilmiş ise tabiri de yoksa kelimeleri parçalayarak en yakın anlamaı bulma----
                    kelimlere_ayir = n.split (" ")
                    tabir_listesi = []
                    kelimlere_ayir2 = [i for i in kelimlere_ayir if i != 'sueño' if i != 'soñado'
                                       if i != 'viendo' if i != 'yo' if i != 'mi' if i != 'soñada']
                    for klm in kelimlere_ayir2:
                        tabir1 = Ruyatabirlerix3.objects.filter (kelime_es__contains=klm)
                        if not tabir1:
                            s = 0
                            while not tabir1:
                                k = len (klm)
                                s += 1
                                k1 = k - s
                                klm1 = klm[:k1]
                                tabir1 = Ruyatabirlerix3.objects.filter (kelime_es__contains=klm1)
                            for i in tabir1:
                                tabir_listesi += [i]
                        else:
                            for i in tabir1:
                                tabir_listesi += [i]
                    tabir1 = tabir_listesi
                    mesaj = "Desafortunadamente, no se ha encontrado la interpretación de los sueños que está buscando. Otras interpretaciones de sueños relacionados se enumeran a continuación."
                    return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'mesaj': mesaj, 'tabir1': tabir1})
            else:
                pass
            form = AramaForm ()
            mesaj = "Por favor, escriba cualquier palabra clave."
            return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'mesaj': mesaj, 'form': form})
        else:
            form = AramaForm ()
            return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'form': form})
    # ----------rusça------
    elif get_language () == 'ru':
        if response.method == "POST":
            form = AramaForm (response.POST)
            if form.is_valid ():
                n1 = form.cleaned_data["kelime"]
                print (n1)
                n = n1.lower ()  # girilen kelime küçük harflere dönüştürüldü
                print (n)
                # ------------Karakter Kontrolü yapıldı. Uygun olmayan varsa hata verildi.-------------
                harfler = 'абвгдеёжзийклмнопрстуфхцчшщъыьэю я'
                for harf in n:
                    if not harf in harfler:
                        mesaj = ' : Пожалуйста, используйте только английские буквы.'
                        return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'n1': n1, 'mesaj': mesaj})
                    else:
                        pass
                # --------------------Karakter Kontrolü bitti----------------
                ArananKelimeler.objects.create (kelime=n)  # aranan kelime kontrollerden sonra db kaydedildi.
                # -----------Aranan kelimenin tabiri db den alında yoksa hata verip en yakın tabir verildi---------
                tabir1 = Ruyatabirlerix3.objects.filter (kelime_ru__contains=n)
                print (tabir1)
                if tabir1:
                    return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'tabir1': tabir1})  # tabir var
                else:
                    # --birden fazla kelime girilmiş ise tabiri de yoksa kelimeleri parçalayarak en yakın anlamaı bulma----
                    kelimlere_ayir = n.split (" ")
                    tabir_listesi = []
                    kelimlere_ayir2 = [i for i in kelimlere_ayir if i != 'мечта' if i != 'снилось'
                                       if i != 'видящий' if i != 'я' if i != 'мой' if i != 'иметь']
                    for klm in kelimlere_ayir2:
                        tabir1 = Ruyatabirlerix3.objects.filter (kelime_ru__contains=klm)
                        if not tabir1:
                            s = 0
                            while not tabir1:
                                k = len (klm)
                                s += 1
                                k1 = k - s
                                klm1 = klm[:k1]
                                tabir1 = Ruyatabirlerix3.objects.filter (kelime_ru__contains=klm1)
                            for i in tabir1:
                                tabir_listesi += [i]
                        else:
                            for i in tabir1:
                                tabir_listesi += [i]
                    tabir1 = tabir_listesi
                    mesaj = "К сожалению, истолкование мечты, которое вы ищете, не найдено. Другие связанные сновидения толкования были перечислены ниже."
                    return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'mesaj': mesaj, 'tabir1': tabir1})
            else:
                pass
            form = AramaForm ()
            mesaj = "Пожалуйста, напишите любые ключевые слова."
            return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'mesaj': mesaj, 'form': form})
        else:
            form = AramaForm ()
            return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'form': form})
    else:  # get_language() == 'tr'
        if response.method == "POST":
            form = AramaForm (response.POST)
            if form.is_valid ():
                n1 = form.cleaned_data["kelime"]
                n = n1.replace ("I", "ı").replace ("İ", "i").lower ()  # girilen kelime küçük harflere dönüştürüldü
                # ------------Karakter Kontrolü yapıldı. Uygun olmayan varsa hata verildi.-------------
                harfler = 'bcçdfgğhjklmnprsştvyzaeıiuüo ö'
                for harf in n:
                    if not harf in harfler:
                        mesaj = ' : Sadece Türkçe Harflerden Oluşmalıdır.'
                        return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'n1': n1, 'mesaj': mesaj})
                    else:
                        pass
                # --------------------Karakter Kontrolü bitti----------------
                ArananKelimeler.objects.create (kelime=n)  # aranan kelime kontrollerden sonra db kaydedildi.
                # -----------Aranan kelimenin tabiri db den alında yoksa hata verip en yakın tabir verildi---------
                tabir1 = Ruyatabirleri.objects.filter (kelime__contains=n)
                if tabir1:
                    return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'tabir1': tabir1})  # tabir var
                else:
                    tabir1=Ruyatabirlerix3.objects.filter(kelime_tr__contains=n)
                    if tabir1:
                        return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'tabir1': tabir1})  # tabir var
                    # --birden fazla kelime girilmiş ise tabiri de yoksa kelimeleri parçalayarak en yakın anlamaı bulma----
                    kelimlere_ayir = n.split (" ")
                    tabir_listesi = []
                    kelimlere_ayir2 = [i for i in kelimlere_ayir if i != 'rüyada' if i != 'görmek'
                                       if i != 'rüyamda' if i != 'ruyada' if i != 'ruyamda' if i != 'gördüm']
                    for klm in kelimlere_ayir2:
                        tabir1 = Ruyatabirleri.objects.filter (kelime__contains=klm)
                        if not tabir1:
                            s = 0
                            while not tabir1:
                                k = len (klm)
                                s += 1
                                k1 = k - s
                                klm1 = klm[:k1]
                                tabir1 = Ruyatabirleri.objects.filter (kelime__contains=klm1)
                            for i in tabir1:
                                tabir_listesi += [i]
                        else:
                            for i in tabir1:
                                tabir_listesi += [i]
                    tabir1 = tabir_listesi
                    mesaj = "Aradığınız rüya yorumu bulunamamıştır. En yakın yorumlar aşağıda listelenmiştir."
                    return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'mesaj': mesaj, 'tabir1': tabir1})
            else:
                pass
            form = AramaForm ()
            mesaj = 'Lütfen Bir Kelime Yazınız.'
            return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'mesaj': mesaj, 'form': form})
        else:
            form = AramaForm ()
            return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'form': form})


def gizlilik(request):
    return render (request, 'ruyatabirleri/anasayfa_gizlilik.html', {})


def ruyatabirleri_ayrinti(response, slug=None):
    if get_language () == 'en':
        tabir1 = get_object_or_404 (Ruyatabirlerix3, kelime_en=slug)
        karakter_satiri = int (len (tabir1.tabiri_en) / 100)
        sayac = 0
        for i in tabir1.tabiri_en:
            if i == "\n":
                sayac += 1
        if len (tabir1.tabiri_en) > 100:
            satir = (sayac + karakter_satiri)
        else:
            satir = (sayac + 2)
        object_pk = tabir1.id
        form = AramaForm ()
        return render (response, 'ruyatabirleri/ruyatabirleri_ayrinti.html',
                       {'satir': satir, 'tabir1': tabir1, 'form': form, 'object_pk': object_pk})

    elif get_language () == 'es':
        tabir1 = get_object_or_404 (Ruyatabirlerix3, slug_es=slug)
        karakter_satiri = int (len (tabir1.tabiri_es) / 100)
        sayac = 0
        for i in tabir1.tabiri_es:
            if i == "\n":
                sayac += 1
        if len (tabir1.tabiri_es) > 100:
            satir = (sayac + karakter_satiri)
        else:
            satir = (sayac + 2)
        object_pk = tabir1.id
        form = AramaForm ()
        return render (response, 'ruyatabirleri/ruyatabirleri_ayrinti.html',
                       {'satir': satir, 'tabir1': tabir1, 'form': form, 'object_pk': object_pk})
    elif get_language () == 'ru':
        tabir1 = get_object_or_404 (Ruyatabirlerix3, slug_ru=slug)
        karakter_satiri = int (len (tabir1.tabiri_ru) / 100)
        sayac = 0
        for i in tabir1.tabiri_ru:
            if i == "\n":
                sayac += 1
        if len (tabir1.tabiri_ru) > 100:
            satir = (sayac + karakter_satiri)
        else:
            satir = (sayac + 2)
        object_pk = tabir1.id
        form = AramaForm ()
        return render (response, 'ruyatabirleri/ruyatabirleri_ayrinti.html',
                       {'satir': satir, 'tabir1': tabir1, 'form': form, 'object_pk': object_pk})

    else:  # get_language() == 'tr'
        tabir1 = Ruyatabirleri.objects.filter (slug=slug)
        if tabir1:
            tablo=1
            tabir1 = get_object_or_404 (Ruyatabirleri, slug=slug)
            karakter_satiri = int (len (tabir1.tabiri) / 100)
            sayac = 0
            for i in tabir1.tabiri:
                if i == "\n":
                    sayac += 1
            if len (tabir1.tabiri) > 100:
                satir = (sayac + karakter_satiri)
            else:
                satir = (sayac + 2)
            object_pk = tabir1.id
            form = AramaForm ()
            return render (response, 'ruyatabirleri/ruyatabirleri_ayrinti.html',
                           {'satir': satir, 'tabir1': tabir1, 'form': form, 'object_pk': object_pk, 'tablo':tablo})
        else:
            tablo:2
            tabir1 = get_object_or_404 (Ruyatabirlerix3, slug_tr=slug)
            karakter_satiri = int (len (tabir1.tabiri_tr) / 100)
            sayac = 0
            for i in tabir1.tabiri_tr:
                if i == "\n":
                    sayac += 1
            if len (tabir1.tabiri_tr) > 100:
                satir = (sayac + karakter_satiri)
            else:
                satir = (sayac + 2)
            object_pk = tabir1.id
            form = AramaForm ()
            return render (response, 'ruyatabirleri/ruyatabirleri_ayrinti.html',
                           {'satir': satir, 'tabir1': tabir1, 'form': form, 'object_pk': object_pk, 'tablo':tablo})


def harf_sayfalari(response, harf):
    tabir1 = Ruyatabirleri.objects.filter (kelime__startswith=harf)
    form = AramaForm ()
    return render (response, 'ruyatabirleri/ruyatabirleri_anasayfa.html', {'tabir1': tabir1, 'form': form})


def anasayfa(request):
    return render (request, 'ruyatabirleri/anasayfa.html', {})


def yildizname_nedir(request):
    return render (request, 'ruyatabirleri/yildizname_nedir.html', {})


def ruyatabirleri_nedir(request):
    return render (request, 'ruyatabirleri/ruyatabirleri_nedir.html', {})


def yildizname(response):
    if response.method == "POST":
        form = YildiznameForm (response.POST)
        if form.is_valid ():
            cinsiyet = form.cleaned_data.get ('cinsiyet')
            isim = form.cleaned_data.get ('isim')
            anne_ismi = form.cleaned_data.get ('anne_ismi')
            # --------girilen harfler küçük harfe dönüştürüldü.---------
            isim = isim.replace ("I", "ı").replace ("İ", "i").lower ()
            anne_ismi = anne_ismi.replace ("I", "ı").replace ("İ", "i").lower ()
            # --------------------------bitti------------------------------------
            # ----Cinsiyet seçiminin yapılması ve isimler için doğru Karakter girilmesi sağlanacak yoksa hata verecek---
            if cinsiyet == "Cinsiyetiniz":
                mesaj = _ ('Lütfen Cinsiyet Seçimini Yapınız')
                form = YildiznameForm ()
                return render (response, 'ruyatabirleri/yildizname.html', {'mesaj': mesaj, 'form': form})
            else:
                pass
            sesli_harfler = 'aeıiuüoö'
            sessiz_harfler = 'bcçdfgğhjklmnprsştvyzwqx'
            harfler = 'bcçdfgğhjklmnprsştvyzaeıiuüo ö'
            if len (isim) < 3 or len (anne_ismi) < 3:
                mesaj = _ ('İsminiz veya anne isminiz çok kısa. Tekrar Deneyiniz.')
                form = YildiznameForm ()
                return render (response, 'ruyatabirleri/yildizname.html', {'mesaj': mesaj, 'form': form})
            else:
                pass
            for harf in isim:
                if not harf in harfler:
                    mesaj = _ ('İsminizde Türkçe Harfler Dışında Karakter Kullanmayınız.')
                    form = YildiznameForm ()
                    return render (response, 'ruyatabirleri/yildizname.html', {'mesaj': mesaj, 'form': form})
                else:
                    pass
            for harf in anne_ismi:
                if not harf in harfler:
                    mesaj = _ ('Anne İsminde Türkçe Harfler Dışında Karakter Kullanmayınız.')
                    form = YildiznameForm ()
                    return render (response, 'ruyatabirleri/yildizname.html', {'mesaj': mesaj, 'form': form})
                else:
                    pass
            # --------------------Karakter Kontrolü bitti----------------

            form.save ()  # karakterler doğru girilmişse db ye kaydediyoruz.

            # ---------------birden fazla isim varsa tespit edilip tüm isimler bir dosyaya yazıldı-----------
            isimler = isim.strip ().split (' ')  # bir den fazla ismi varsa boşluktan bölerek her birini elde ediyoruz
            hesap_kutusu = []  # üç harften küçük kelimeleri eliyoruz kalanları buraya yazıyoruz
            for i in range (len (isimler)):
                if not len (isimler[i]) < 3:
                    hesap_kutusu += [isimler[i]]

            anne_isimleri = anne_ismi.strip ().split (
                ' ')  # bir den fazla ismi varsa boşluktan bölerek her birini elde ediyoruz
            for i in range (len (anne_isimleri)):
                if not len (anne_isimleri[i]) < 3:
                    hesap_kutusu += [anne_isimleri[i]]

            # ---------------EBCED hesabı Yapılacak.------------------------
            harf_degerleri = {'a': 1, 'b': 2, 'c': 3, 'ç': 3, 'd': 4, 'e': 1, 'f': 8, 'g': 8, 'ğ': 4, 'h': 5, 'ı': 1,
                              'i': 1,
                              'j': 7, 'k': 4, 'l': 6, 'm': 4, 'n': 2, 'o': 7, 'ö': 7, 'p': 2, 'r': 8, 's': 0, 'ş': 0,
                              't': 4, 'u': 7, 'ü': 7, 'v': 6, 'y': 10, 'z': 7, }

            toplanacak_harfler = ""
            harflerin_toplami = 0

            for i in range (len (hesap_kutusu)):
                for z in range (len (hesap_kutusu[i])):
                    if hesap_kutusu[i][z] in sessiz_harfler:
                        toplanacak_harfler += hesap_kutusu[i][z]

            for i in range (len (hesap_kutusu)):
                if hesap_kutusu[i][0] in sesli_harfler:
                    toplanacak_harfler += hesap_kutusu[i][0]

            print (toplanacak_harfler)

            for i in toplanacak_harfler:
                harflerin_toplami += harf_degerleri[i]
            print (harflerin_toplami)

            mod = (harflerin_toplami) % 12
            print (mod)
            # -----------EBCED Hesabı Bitti. Mod Bulundu.---------------
            return render (response, 'ruyatabirleri/yildizname_sonuc.html', {'cinsiyet': cinsiyet, 'mod': mod})
        mesaj = _ ('Lütfen Formu Doldurunuz.')
        return render (response, 'ruyatabirleri/yildizname.html', {'form': form, 'mesaj': mesaj})
    else:
        form = YildiznameForm ()
        return render (response, 'ruyatabirleri/yildizname.html', {'form': form})


def iletisim(response):
    if response.method == "POST":
        form = RtxiletisimForm (response.POST)
        if form.is_valid ():
            isim = form.cleaned_data.get ('isim')
            soy_isim = form.cleaned_data.get ('soy_isim')
            eposta = form.cleaned_data.get ('eposta')
            ileti = form.cleaned_data.get ('mesaj')
            # ----Tüm kutucukların doldurulması sağlandı yoksa hata verecek---
            if len (isim) < 1 or len (soy_isim) < 1 or len (eposta) < 1 or len (ileti) < 1:
                mesaj = _ ('Kutucukları Doldurunuz.')
                form = RtxiletisimForm ()
                return render (response, 'ruyatabirleri/anasayfa_iletisim.html', {'mesaj': mesaj, 'form': form})
            else:
                pass
            # --------------------kutu Kontrolü bitti----------------
            form.save ()
            mesaj = _ ("Gönderiniz başarıyla kaydedildi.")
            form = RtxiletisimForm ()
            return render (response, 'ruyatabirleri/anasayfa_iletisim.html',
                           {'form': form, 'mesaj': mesaj})
        mesaj = _ ('Lütfen Formu Doldurunuz.')
        return render (response, 'ruyatabirleri/anasayfa_iletisim.html', {'form': form, 'mesaj': mesaj})
    else:
        form = RtxiletisimForm ()
        return render (response, 'ruyatabirleri/anasayfa_iletisim.html', {'form': form})


def tefeul(request):
    besmele = KuranBilgi.objects.get (id=1)  # besmele
    return render (request, 'ruyatabirleri/tefeul.html', {'besmele': besmele})


def tefeul_yap(request):
    besmele = KuranBilgi.objects.get (id=1)  # besmele
    # hangi_sure = random.randint (1, 114)
    hangi_sure = 1
    bilgi_satiri = KuranBilgi.objects.filter (sure_no=hangi_sure)
    for item in bilgi_satiri:
        x1 = item.ayet_say
        hangi_ayet = random.randint (1, x1)
        bilgi_satiri_2 = KuranBilgi.objects.filter (sure_no=hangi_sure).filter (ayet_no=hangi_ayet)
        kelime_sayisi = KuranKelime.objects.filter (sure_no=hangi_sure).filter (ayet_no=hangi_ayet).count ()
        hangi_kelime = random.randint (1, kelime_sayisi)
        bilgi_satiri_3 = KuranKelime.objects.filter (sure_no=hangi_sure).filter (ayet_no=hangi_ayet).filter (
            kelime_no=hangi_kelime)
        return render (request, 'ruyatabirleri/tefeul.html',
                       {'besmele': besmele, 'bilgi_satiri_2': bilgi_satiri_2, 'hangi_kelime': hangi_kelime,
                        'bilgi_satiri_3': bilgi_satiri_3})


def tefeul_nedir(request):
    return render (request, 'ruyatabirleri/tefeul_nedir.html', {})


def dua(request):
    return render (request, 'ruyatabirleri/dua.html', {})


def dua_nedir(request):
    return render (request, 'ruyatabirleri/dua_nedir.html', {})


def ruyatabirleri_ayrinti_sbt_syf(response, slug=None):
    tabir1 = get_object_or_404 (Ruyatabirlerix_sbt, slug=slug)
    return render (response, 'ruyatabirleri/ruyatabirleri_ayrinti.html', {'tabir1': tabir1})


def rtx_yorum(response):
    if response.method == "POST":
        form = RTXYorumForm (response.POST)
        if form.is_valid ():
            isim = form.cleaned_data.get ('isim')
            soy_isim = form.cleaned_data.get ('soy_isim')
            cinsiyet = form.cleaned_data.get ('cinsiyet')
            eposta = form.cleaned_data.get ('eposta')
            eposta1 = form.cleaned_data.get ('eposta1')
            ruya_zamani = form.cleaned_data.get ('ruya_zamani')
            bilinc_alti = form.cleaned_data.get ('bilinc_alti')
            ruya = form.cleaned_data.get ('ruya')

            if eposta == eposta1:
                form.save ()
                mesaj = _ ("Gönderiniz başarıyla kaydedildi.")
                form = RTXYorumForm ()
                return render (response, 'ruyatabirleri/ruyatabirleri_yorum.html', {'form': form, 'mesaj': mesaj})
            else:
                mesaj = _ ('Yazdığınız eposta adresleri birbirinden farklıdır. Aynı olması gerekmektedir. Lütfen düzeltiniz.')
                form = RTXYorumForm ()
                return render (response, 'ruyatabirleri/ruyatabirleri_yorum.html', {'mesaj': mesaj, 'form': form})
        mesaj = _ ('Lütfen Formu Doldurunuz.')
        return render (response, 'ruyatabirleri/ruyatabirleri_yorum.html', {'form': form, 'mesaj': mesaj})
    else:
        form = RTXYorumForm ()
        return render (response, 'ruyatabirleri/ruyatabirleri_yorum.html', {'form': form})


def rtx_ara_yorum(response):
    return render(response, 'ruyatabirleri/ruyatabirleri_ara_yorum.html', {})

def yonetici(response):
    ruya_tabiri_alt_ref = Ruyatabirlerix3.objects.all()
    sbt_syf = Ruyatabirlerix_sbt.objects.all ()
    iletisim_list = Rtx_iletisim.objects.all ()
    gond_ruya_tabiri = RTXyorum.objects.all ()
    return render(response, 'ruyatabirleri/anasayfa_yonetici.html', {'ruya_tabiri_alt_ref':ruya_tabiri_alt_ref,
                                                                     'iletisim_list':iletisim_list,
                                                                     'sbt_syf':sbt_syf,
                                                                     'gond_ruya_tabiri':gond_ruya_tabiri})