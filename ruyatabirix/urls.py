from django.contrib import admin
from django.urls import path, include
from ruyatabirleri.models import Ruyatabirleri
import ruyatabirleri.views

from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from ruyatabirleri.sitemaps import StaticViewSitemap

sitemaps = {
    'ruyatabirleri': GenericSitemap({
        'queryset': Ruyatabirleri.objects.all(),
        'date_field': 'updated',
    }, priority=0.9),
    'static': StaticViewSitemap,
}

urlpatterns = [
    path ('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path ('w2e3r4t5_admin/', admin.site.urls),
    path ('', include ('ruyatabirleri.urls')),
    path ('register/', include('register.urls')),
    path ('comments/', include('django_comments.urls')),
]
