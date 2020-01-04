from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'style': 'width: 300px; height: 50px;'
                            ' font-size: 20px;','placeholder': 'Şifreniz', }),)
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'style': 'width: 300px; height: 50px;'
                            ' font-size: 20px;','placeholder': 'Şifrenizi Tekrar Giriniz', }),)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

        labels = {'username': '', 'first_name': '', 'last_name': '', 'email': '', 'password1': '', 'password2': '',}
        help_texts = {'username': '', 'first_name': '', 'last_name': '', 'email': '', 'password1': '', 'password2': '',}
        error_messages = {'username': {'max_length': "This is too long",},}
        widgets = {'username': forms.TextInput (attrs={'style': 'width: 300px; height: 50px; font-size: 20px;',
                                                    'placeholder': 'Kullanıcı Adınız', }),
                   'first_name': forms.TextInput (attrs={'style': 'width: 300px; height: 50px; font-size: 20px;',
                                                    'placeholder': 'Adınız',}),
                   'last_name': forms.TextInput (attrs={'style': 'width: 300px; height: 50px; font-size: 20px;',
                                                    'placeholder': 'Soyadınız',}),
                   'email': forms.EmailInput (attrs={'style': 'width: 300px; height: 50px; font-size: 20px;',
                                                    'placeholder': 'Eposta Adresiniz',}),
                   }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label='', widget=forms.TextInput(attrs={'style': 'width: 300px; height: 50px;'
                            ' font-size: 20px;','placeholder': 'Kullanıcı Adınız',}))
    password = forms.CharField(label= '', widget=forms.PasswordInput(attrs={'style': 'width: 300px; height: 50px;'
                            ' font-size: 20px;','placeholder': 'Şifreniz',}))

    class Meta:
        model = User
        fields = ('username', 'password',)

        help_texts = {'username': '', 'first_name': '', 'last_name': '', 'email': '', 'password1': '', 'password2': '',}
        error_messages = {'username': {'max_length': "This is too long",},}
