from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Ruyatabirleri (models.Model):
    kelime = models.CharField(max_length=200)
    slug = models.SlugField (blank=True, null=True)
    tabiri = models.TextField ()
    ekleme_tarihi = models.DateTimeField(auto_now_add=True)
    aranma_sayisi = models.IntegerField(null=True)
    ingilizce_kelime = models.CharField(max_length=200, null=True)
    ingilizce_tabir = models.TextField(null=True)

    def __str__(self):
        return str(self.slug)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.kelime)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse ('ruyatabirleri:ruyatabirleri_ayrinti', args=[str(self.slug)])

class ArananKelimeler (models.Model):
    kelime = models.CharField(max_length=200)
    uygunluk_onayi = models.BooleanField (default=False)
    def __str__(self):
        return self.kelime