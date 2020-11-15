from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap as sitemaps_sitemap
from ruyatabirleri.sitemap import (
    foo_static_sitemap,
    FooItemAlternateHreflangSitemap2,
    FooItemAlternateHreflangSitemap,
)
from django.views.generic.base import RedirectView, TemplateView
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

sitemaps = {
    'foo-items-alternate-hreflang': FooItemAlternateHreflangSitemap,
    'foo-items-alternate-hreflang2': FooItemAlternateHreflangSitemap2,
    'foo-static': foo_static_sitemap,
}

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path ('w2e3r4t5_admin/', admin.site.urls),
    path('sitemap.xml/', sitemaps_sitemap, {'sitemaps': sitemaps, 'template_name': 'ruyatabirleri/rel_alternate_hreflang_sitemap.xml'}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^favicon\.ico$', favicon_view),
    path('robots.txt', TemplateView.as_view (template_name="ruyatabirleri/robots.txt", content_type="text/plain"),),
]

urlpatterns += i18n_patterns(
    path('', include('ruyatabirleri.urls')),
    path ('register/', include('register.urls')),
    path ('comments/', include('django_comments.urls')),
    prefix_default_language=False,
)