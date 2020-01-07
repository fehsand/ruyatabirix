from django import forms
from .models import ArananKelimeler


class AramaForm (forms.ModelForm):

    class Meta:
        model = ArananKelimeler
        fields = ('kelime',)

        labels = { 'kelime': '',}
        error_messages = {'kelime': {'max_length': "This is too long",},}
        widgets = { 'kelime': forms.TextInput (attrs={'style': 'border-style: none; width: 400px; font-size: 20px; padding: 15px 10px;',
                                                    'placeholder': 'Aramak İstediğiniz Kelimeyi Yazınız.',}),}