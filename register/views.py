from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

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
            return render (request, 'register/hesap.html', {})
    else:
        form = SignUpForm()
    return render(request, 'register/register.html', {'form': form})