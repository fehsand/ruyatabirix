from django import forms
from .models import ArananKelimeler


class AramaForm (forms.ModelForm):

    class Meta:
        model = ArananKelimeler
        fields = ('kelime',)