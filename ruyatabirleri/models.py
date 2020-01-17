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

