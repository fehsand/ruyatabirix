from django import forms
from .models import ArananKelimeler


class AramaForm (forms.ModelForm):

    class Meta:
        model = ArananKelimeler
        fields = ('kelime',)

        labels = { 'kelime': '',}
        error_messages = {'kelime': {'max_length': "This is too long",},}
        widgets = { 'kelime': forms.TextInput (attrs={'style': 'width: 400px; font-size: 20px; padding: 15px 10px;',
                                                    'placeholder': 'Aramak İstediğiniz Kelimeyi Yazınız.',}),}


"""
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        labels = { 'author': '', 'text': '',}
        error_messages = {'author': {'max_length': "This is too long",},}
        widgets = { 'author': forms.TextInput (attrs={'style': 'width: 500px; font-size: 20px;',
                                                    'placeholder': 'Yazar',}),
                    'text': forms.Textarea (attrs={'style': 'width: 500px; font-size: 20px;',
                                                      'placeholder': 'Yorum Yaz', }), }

"""