from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from ruyatabirleri.sitemaps import RuyatabirleriSitemap, StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap, 'ruyatabirleri': RuyatabirleriSitemap
}

urlpatterns = [
    path ('admin/', admin.site.urls),
    path ('', include ('ruyatabirleri.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path ('register/', include('register.urls')),
    path ('comments/', include('django_comments.urls')),

]
