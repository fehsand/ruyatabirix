from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views

app_name = "register"
urlpatterns = [
    path (' ', views.register, name='register'),
    path ('basarili_kayit/', views.basarili_kayit, name='basarili_kayit'),
    path ('basarili_giris/', views.basarili_giris, name='basarili_giris'),
    path ('basarili_cikis/', views.basarili_cikis, name='basarili_cikis'),
    path ('hesap/', views.hesap, name='hesap'),
    path ('accounts/', include ("django.contrib.auth.urls")),
    path ('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]