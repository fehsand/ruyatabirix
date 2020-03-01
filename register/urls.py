from django.urls import path, include
from .import views

app_name = "register"
urlpatterns = [
    path (' ', views.register, name='register'),
    path ('accounts/', include ("django.contrib.auth.urls")),
    path ('hesap/', views.hesap, name='hesap'),
]