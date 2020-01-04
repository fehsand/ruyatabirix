from django.shortcuts import render, redirect
from .forms import SignUpForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def basarili_kayit (request):
    return render(request, 'register/basarili_kayit.html', {})
def basarili_giris (request):
    return render(request, 'register/basarili_giris.html', {})
def basarili_cikis (request):
    return render(request, 'register/basarili_cikis.html', {})
def hesap (request):
    return render(request, 'register/hesap.html', {})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render (request, 'register/basarili_kayit.html', {'username': username})
    else:
        form = SignUpForm()
    return render(request, 'register/register.html', {'form': form})

def LoginView(request):
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = UserLoginForm()
    return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})


#@login_required