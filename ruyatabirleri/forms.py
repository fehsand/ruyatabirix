from django import forms
from .models import ArananKelimeler, yildizname, RTXyorum

#iletisim,

class AramaForm (forms.ModelForm):

    class Meta:
        model = ArananKelimeler
        fields = ('kelime',)

class YildiznameForm(forms.ModelForm):

    class Meta:
        model = yildizname
        fields = ('cinsiyet', 'isim', 'anne_ismi',)



class RTXYorumForm(forms.ModelForm):

    class Meta:
        model = RTXyorum
        fields = ('isim', 'soy_isim', 'cinsiyet', 'eposta', 'eposta1',
                  'ruya_zamani', 'bilinc_alti', 'ruya', 'geri_donus',)