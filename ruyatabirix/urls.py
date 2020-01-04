from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include ('ruyatabirleri.urls')),
    #path ('register/', include('register.urls')),
    #path ('comments/', include('django_comments.urls')),
]
