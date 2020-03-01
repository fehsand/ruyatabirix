from django import forms
from .models import ArananKelimeler, yildizname, iletisim

class AramaForm (forms.ModelForm):

    class Meta:
        model = ArananKelimeler
        fields = ('kelime',)

class YildiznameForm(forms.ModelForm):

    class Meta:
        model = yildizname
        fields = ('cinsiyet', 'isim', 'anne_ismi',)

class iletisimForm(forms.ModelForm):

    class Meta:
        model = iletisim
        fields = ('isim', 'soy_isim', 'eposta', 'mesaj',)
