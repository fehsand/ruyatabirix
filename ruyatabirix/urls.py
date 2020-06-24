from django.contrib import admin
from django.urls import path, include
from ruyatabirleri.models import Ruyatabirleri

from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from ruyatabirleri.sitemaps import StaticViewSitemap

from django.conf.urls.i18n import i18n_patterns

sitemaps = {
    'ruyatabirleri': GenericSitemap({
        'queryset': Ruyatabirleri.objects.all(),
        'date_field': 'updated',
    }, priority=0.9),
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path ('w2e3r4t5_admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path ('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('ruyatabirleri.urls')),
    path ('register/', include('register.urls')),
    path ('comments/', include('django_comments.urls')),
    prefix_default_language=False,
)