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