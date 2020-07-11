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

class iletisim (models.Model):
    isim = models.CharField(max_length=200)
    soy_isim = models.CharField(max_length=200)
    eposta = models.EmailField(max_length=200)
    mesaj = models.TextField()

    def __str__(self):
        return self.mesaj

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

class Ruyatabirlerix (models.Model):
    kelime = models.CharField (default='', max_length=255)
    slug = models.SlugField (default='', blank=True, max_length=255)
    tabiri = models.TextField ()
    ekleme_tarihi = models.DateTimeField(auto_now_add=True)
    aranma_sayisi = models.IntegerField(null=True)
    kelime_en = models.CharField(max_length=200, null=True)
    tabir_en = models.TextField(null=True)
    altr_en_url = models.URLField (blank=True, null=True)
    kelime_ar = models.CharField(max_length=200, null=True)
    tabir_ar = models.TextField(null=True)
    altr_ar_url = models.URLField (blank=True, null=True)
    kelime_ru = models.CharField(max_length=200, null=True)
    slug_ru = models.SlugField (default='', blank=True, max_length=255, allow_unicode=True)
    tabir_ru = models.TextField(null=True)
    altr_ru_url = models.URLField (blank=True, null=True)
    kelime_es = models.CharField(max_length=200, null=True)
    tabir_es = models.TextField(null=True)
    altr_es_url = models.URLField (blank=True, null=True)
    kelime_ch = models.CharField(max_length=200, null=True)
    tabir_ch = models.TextField(null=True)
    altr_ch_url = models.URLField (blank=True, null=True)
    updated = models.DateTimeField (auto_now=True, null=True)

    def __str__(self):
        return self.kelime

    def save(self, *args, **kwargs):
        self.slug = slugify(self.kelime.replace('ı','i'))
        self.slug_ru = slugify(self.kelime_ru.replace('у','y').replace('ё','e').replace('х','h').replace('щ','sch').replace('а', 'a').replace('б','b').replace('в','v').replace('г','g').replace('д','d').replace('е','e').replace('ё','e').replace('ж','zh').replace('з','z').replace('и','i').replace('й','y').replace('к','k').replace('л','l').replace('м','m').replace('н','n').replace('о','o').replace('п','p').replace('р','r').replace('с','s').replace('т','t').replace('у','u').replace('ф','f').replace('х','h').replace('ц','ts').replace('ч','ch').replace('ш','sh').replace('щ','sch').replace('ъ','').replace('ы','y').replace('ь','').replace('э','e').replace('ю','yu').replace('я','ya').replace('ю','u').replace('я','ya'), allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse ('ruyatabirleri:ruyatabirleri_ayrinti',
                        args=[str(self.slug)])

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



class Ruyatabirlerix3 (models.Model):
    kelime_tr = models.CharField(max_length=255)
    slug_tr = models.SlugField(unique=True, blank=True, max_length=255)
    tabiri_tr = models.TextField()
    kelime_en = models.CharField(max_length=200)
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
    ekleme_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kelime_tr

    def save(self, *args, **kwargs):
        self.slug_tr = slugify(self.kelime_tr.replace('ı','i'))
        self.slug_es = slugify(self.kelime_es)
        self.slug_ru = slugify(self.kelime_ru.replace('а', 'a').replace('о','o').replace('м','m').replace('т','t').replace('к','k').replace('е','ye').replace('с','s').replace('и','i').replace('д','d').replace('п','p').replace('б','b').replace('л','l').replace('г','g').replace('ш','sh').replace('ж','zh').replace('щ','sch').replace('э','e').replace('я','ya').replace('ф','f').replace('ч','ch').replace('з','z').replace('ю','yu').replace('ц','ts').replace('й','y').replace('ё','yo').replace('в','v').replace('н','n').replace('р','r').replace('у','u').replace('х','h').replace('ъ','').replace('ь','').replace('ы','y'), allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ruyatabirleri:ruyatabirleri_ayrinti',
                        args=[str(self.slug_tr)])