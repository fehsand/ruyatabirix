from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Ruyatabirleri (models.Model):
    kelime = models.CharField (default='', max_length=255)
    slug = models.SlugField (default='', blank=True, max_length=255)
    tabiri = models.TextField ()
    ekleme_tarihi = models.DateTimeField(auto_now_add=True)
    aranma_sayisi = models.IntegerField(null=True)
    ingilizce_kelime = models.CharField(max_length=200, null=True)
    ingilizce_tabir = models.TextField(null=True)
    updated = models.DateTimeField (auto_now=True, null=True)

    def __str__(self):
        return self.kelime

    def save(self, *args, **kwargs):
        self.slug = slugify(self.kelime.replace('ı','i'))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse ('ruyatabirleri:ruyatabirleri_ayrinti',
                        args=[str(self.slug)])

class ArananKelimeler (models.Model):
    kelime = models.CharField(max_length=200)
    uygunluk_onayi = models.BooleanField (default=False)
    def __str__(self):
        return self.kelime

class yildizname (models.Model):
    isim = models.CharField (max_length=200)
    anne_ismi = models.CharField(max_length=200)
    cinsiyet = models.CharField(max_length=200)

    def __str__(self):
        return self.isim

class Rtx_iletisim (models.Model):
    isim = models.CharField(max_length=200, help_text="Lütfen İsminizi Yazınız")
    soy_isim = models.CharField(max_length=200, help_text="Lütfen Soyisminizi Yazınız")
    eposta = models.EmailField(max_length=200, help_text="Lütfen Eposta Adresinizi Yazınız.")
    eposta1 = models.EmailField(null=True, max_length=200, help_text="Lütfen Eposta Adresinizi Doğrulayınız.")
    mesaj = models.TextField(help_text='Mesajınızı yazınız')
    kayit_tarihi = models.DateTimeField(null=True, auto_now_add=True)
    geri_donus = models.BooleanField (default=False, help_text="Cevap verilen mesajlar true yapılacak")
    cevap = models.TextField(null=True, help_text="Cevap metni buraya yazılacak")

    def __str__(self):
        return self.eposta

class KuranBilgi (models.Model):
    sure_no = models.IntegerField()
    sure_isim = models.CharField(max_length=200)
    ayet_say = models.IntegerField()
    ayet_no = models.IntegerField()
    ayet = models.TextField()
    ayet_meal = models.TextField()

    def __str__(self):
        return self.sure_isim

class KuranKelime (models.Model):
    sure_no = models.IntegerField()
    ayet_no = models.IntegerField()
    kelime_no = models.IntegerField()
    kelime_arapca = models.CharField(max_length=200)
    kelime_turkce = models.CharField (max_length=200)

    def __str__(self):
        return self.kelime_turkce

class Ruyatabirlerix_sbt (models.Model):
    kelime = models.CharField (default='', max_length=255)
    slug = models.SlugField (default='', blank=True, max_length=255)
    ekleme_tarihi = models.DateTimeField(auto_now_add=True)
    altr_en_url = models.URLField (blank=True, null=True)
    altr_ar_url = models.URLField (blank=True, null=True)
    altr_ru_url = models.URLField (blank=True, null=True)
    altr_es_url = models.URLField (blank=True, null=True)
    altr_ch_url = models.URLField (blank=True, null=True)
    updated = models.DateTimeField (auto_now=True, null=True)

    def __str__(self):
        return self.kelime

    def save(self, *args, **kwargs):
        self.slug = slugify(self.kelime.replace('ı','i'))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse ('ruyatabirleri:ruyatabirleri_ayrinti_sbt_syf',
                        args=[str(self.slug)])

class RTXyorum (models.Model):
    isim = models.CharField(max_length=200, help_text="Lütfen İsminizi Yazınız")
    soy_isim = models.CharField(max_length=200, help_text="Lütfen Soyisminizi Yazınız")
    cinsiyet = models.CharField(max_length=10, help_text="Lütfen Cinsiyetinizi Belirtiniz.")
    eposta = models.EmailField(max_length=200, help_text="Lütfen Eposta Adresinizi Yazınız.")
    eposta1 = models.EmailField(max_length=200, help_text="Lütfen Eposta Adresinizi Doğrulayınız.")
    ruya_zamani = models.CharField(null=True, max_length=200, help_text="Lütfen rüyayı ne zaman gördüğünüzü belirtiniz.")
    bilinc_alti = models.CharField(max_length=200, help_text="Yatmadan önce veya gün içerisinde gördüğünüz rüya ile ilgili bir olay yaşadınız mı? veya hayal kurdunuz mu?")
    ruya = models.TextField(help_text="Lütfen rüyanızı basit cümlelerle ayrıntılı olarak anlatınız. Cümlelerin sonuna nokta işareti koymayı unutmayınızı.")
    kayit_tarihi = models.DateTimeField(null=True, auto_now_add=True)
    geri_donus = models.BooleanField (default=False, help_text="Cevap yazılan rüya tabirleri true yapılacak")
    cevap = models.TextField(null=True, help_text="Buraya gönderilen rüya yorumları yazılacak")

    def __str__(self):
        return self.eposta


class Ruyatabirlerix5 (models.Model):
    kelime_tr = models.CharField(max_length=255)
    slug_tr = models.SlugField(unique=True, blank=True, max_length=255, allow_unicode=True)
    tabiri_tr = models.TextField()
    kelime_en = models.CharField(max_length=200)
    slug_en = models.SlugField (unique=True, blank=True, max_length=255)
    tabiri_en = models.TextField()
    altr_en_url = models.URLField(blank=True)
    kelime_es = models.CharField(max_length=200)
    slug_es = models.SlugField(unique=True, blank=True, max_length=255, allow_unicode=True)
    tabiri_es = models.TextField()
    altr_es_url = models.URLField(blank=True)
    kelime_ru = models.CharField(max_length=200, null=True)
    slug_ru = models.SlugField(unique=True, blank=True, max_length=255, allow_unicode=True)
    tabiri_ru = models.TextField(null=True)
    altr_ru_url = models.URLField(blank=True)
    kelime_ar = models.CharField(max_length=200, null=True)
    slug_ar = models.SlugField(unique=True, blank=True, max_length=255, allow_unicode=True)
    tabiri_ar = models.TextField(null=True)
    altr_ar_url = models.URLField(blank=True)
    kelime_ch = models.CharField(max_length=200, null=True)
    slug_ch = models.SlugField(unique=True, blank=True, max_length=255, allow_unicode=True)
    tabiri_ch = models.TextField(null=True)
    altr_ch_url = models.URLField(blank=True)
    ekleme_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kelime_tr

    def save(self, *args, **kwargs):
        self.slug_tr = slugify(self.kelime_tr.replace('ı','i'))
        self.slug_en = slugify (self.kelime_en)
        self.slug_es = slugify(self.kelime_es, allow_unicode=True)
        self.slug_ru = slugify(self.kelime_ru, allow_unicode=True)
        self.slug_ar = slugify (self.kelime_ar, allow_unicode=True)
        self.slug_ch = slugify (self.kelime_ch, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ruyatabirleri:ruyatabirleri_ayrinti_2',
                        args=[str(self.slug_tr)])